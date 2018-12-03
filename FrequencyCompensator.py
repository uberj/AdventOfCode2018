
class FrequencyCompensator(object):
    total_offset = 0

    def compensate_from_input(self, input_):
        for offset in input_.split():
            self.compensate_step(offset)
        return self.total_offset

    def compensate_step(self, offset):
        direction, s = offset[0].strip(), offset[1:].strip()
        if direction == "-":
            self.total_offset -= int(s)
        else:
            self.total_offset += int(s)

        return self.total_offset

    def detect_cycle(self, input_):
        seen = set()
        fg = frequency_generator(input_)
        fc = FrequencyCompensator()

        seen.add(fc.total_offset)
        for f in fg:
            fc.compensate_step(f)
            if fc.total_offset in seen:
                return fc.total_offset
            seen.add(fc.total_offset)


def frequency_generator(input_):
    while True:
        for offset in input_.split():
            yield offset


def challenge1():
    with open("inputs/1.txt", "r") as fd:
        fc = FrequencyCompensator()
        print(fc.compensate_from_input(fd.read()))


def challenge2():
    with open("inputs/1.txt", "r") as fd:
        fc = FrequencyCompensator()
        return fc.detect_cycle(fd.read())



if __name__ == "__main__":
    print(challenge2())
