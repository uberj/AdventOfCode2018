from pprint import pprint
import pdb


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


def calculate_next(next_candidates, reverse_instructions):
    for candidate in next_candidates:
        pre_requisites = reverse_instructions.get(candidate, [])
        is_okay = True
        for non_candidate in filter(lambda x: x != candidate, next_candidates):
            if non_candidate in pre_requisites:
                is_okay = False

        if is_okay:
            return candidate


def step_order(step_lines):
    instructions, reverse_instructions = parse_step_structure(step_lines)

    next_candidates = instructions.keys()
    order = ""
    while True:
        next_candidates = list(sorted(list(set(next_candidates))))
        cur_step = calculate_next(next_candidates, reverse_instructions)
        next_candidates.remove(cur_step)
        order += cur_step
        remove_from_instructions(cur_step, instructions)
        next_candidates += instructions.get(cur_step, [])
        if not next_candidates:
            break

    return order


def challenge1():
    with open("inputs/steps.txt", "r") as fd:
        return step_order(fd.read().strip().split("\n"))


def challenge2():
    with open("inputs/steps.txt", "r") as fd:
        pass


if __name__ == "__main__":
    test = step_order("""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".split("\n"))
    assert "CABDFE" == test, test
    c1 = challenge1()
    assert "IJLFUVDACEHGRZPNKQWSBTMXOY" == c1
    print(c1)
    #print(challenge2())
