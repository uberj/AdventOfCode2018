class BoxChecksum(object):
    def checksum_boxes(self, input_):
        two_count = 0
        three_count = 0
        for label in input_.split():
            letters = set(label)
            two_counted = False
            three_counted = False
            for letter in letters:
                letter_count = len(list(filter(lambda c: c == letter, label)))
                if not two_counted and letter_count == 2:
                    two_counted = True
                    two_count += 1

                if not three_counted and letter_count == 3:
                    three_counted = True
                    three_count += 1

        return two_count * three_count

    def detect_neighbors(self, input_):
        seen = []
        for label in input_.split():
            l = list(label)
            for i in range(len(l)):
                identity = list(l)
                identity[i] = None
                if identity in seen:
                    l.pop(i)
                    return "".join(l)
                seen.append(identity)


def challenge1():
    with open("inputs/box-letters.txt", "r") as fd:
        bc = BoxChecksum()
        print(bc.checksum_boxes(fd.read()))


def challenge2():
    with open("inputs/box-letters.txt", "r") as fd:
        bc = BoxChecksum()
        return bc.detect_neighbors(fd.read())


if __name__ == "__main__":
    print(challenge2())
