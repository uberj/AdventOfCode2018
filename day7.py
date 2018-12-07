from functools import reduce


def parse_step_structure(step_lines):
    instructions = {}
    reverse_instructions = {}
    for line in step_lines:
        step1, step2 = line.split(" must be finished before step ")
        step1 = step1[-1]
        step2 = step2[0]
        instructions.setdefault(step1, []).append(step2)
        reverse_instructions.setdefault(step2, []).append(step1)
    return instructions, reverse_instructions


def remove_from_instructions(cur_step, instructions):
    for values in instructions.values():
        if cur_step in values:
            values.remove(cur_step)


class WorkQueue(object):
    def __init__(self, instructions, reverse_instructions):
        self.instructions = instructions
        self.reverse_instructions = reverse_instructions
        self.next_candidates = self.instructions.keys()
        self.pending = []

    def calculate_ready(self):
        ready = []
        for candidate in self.next_candidates:
            pre_requisites = self.reverse_instructions.get(candidate, [])
            is_okay = True
            for non_candidate in filter(lambda x: x != candidate, self.next_candidates):
                if non_candidate in pre_requisites:
                    is_okay = False

            if is_okay:
                ready.append(candidate)
        return ready


    def mark_complete(self, cur_step):
        self.next_candidates.remove(cur_step)
        remove_from_instructions(cur_step, self.instructions)
        self.next_candidates += self.instructions.get(cur_step, [])
        self.pending.remove(cur_step)

    def next_but_not_complete(self):
        self.next_candidates = list(sorted(list(set(self.next_candidates))))
        if not self.next_candidates:
            return None

        for s in range(len(self.next_candidates)):
            for ready_step in self.calculate_ready():
                if ready_step in self.pending:
                    continue

                self.pending.append(ready_step)
                return ready_step

    def next_mark_complete(self):
        self.next_candidates = list(sorted(list(set(self.next_candidates))))
        if not self.next_candidates:
            return None

        cur_step = self.calculate_ready()[0]
        self.next_candidates.remove(cur_step)
        remove_from_instructions(cur_step, self.instructions)
        self.next_candidates += self.instructions.get(cur_step, [])
        return cur_step


def step_order(step_lines):
    instructions, reverse_instructions = parse_step_structure(step_lines)
    wq = WorkQueue(instructions, reverse_instructions)
    order = ""
    while True:
        step = wq.next_mark_complete()
        if not step:
            break
        order += step
    return order


def time_cost(param, num_workers=2, base_cost=0):
    clock = 0
    num_workers = num_workers
    workers_state = []
    for worker in range(num_workers):
        ws = {'time-remaining': 0, 'work': None}
        workers_state.append(ws)

    instructions, reverse_instructions = parse_step_structure(param)
    wq = WorkQueue(instructions, reverse_instructions)
    while True:
        for worker_number in range(num_workers):
            ws = workers_state[worker_number]
            if ws['time-remaining'] == 0:
                if ws['work']:
                    wq.mark_complete(ws['work'])
                    ws['work'] = wq.next_but_not_complete()
                else:
                    ws['work'] = wq.next_but_not_complete()

                if ws['work']:
                    ws['time-remaining'] = ord(ws['work']) - 64 + base_cost

            if ws['work']:
                ws['time-remaining'] -= 1

        if reduce(lambda a, b: a and b, map(lambda w: w['work'] is None, workers_state)):
            break

        clock += 1

    return clock


def challenge1():
    with open("inputs/steps.txt", "r") as fd:
        return step_order(fd.read().strip().split("\n"))


def challenge2():
    with open("inputs/steps.txt", "r") as fd:
        return time_cost(fd.read().strip().split("\n"), base_cost=60, num_workers=5)


if __name__ == "__main__":
    input_ = step_order("""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".split("\n"))
    test = "".join(input_)
    assert "CABDFE" == test, test
    c1 = "".join(challenge1())
    assert "IJLFUVDACEHGRZPNKQWSBTMXOY" == c1

    t = time_cost("""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".split("\n"), base_cost=0)
    assert 15 == t, t

    c2 = challenge2()
    assert c2, 1072
