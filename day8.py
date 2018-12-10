def challenge1():
    with open("inputs/license.txt", "r") as fd:
        return sum_meta(fd.read())


def challenge2():
    with open("inputs/license.txt", "r") as fd:
        pass


def build_tree(param):
    param.split(" ")
    pass


def sum_meta(param):
    param = list(map(int, param.split(" ")))
    return _sum_meta(param)


def _sum_meta(param):
    num_children = param.pop(0)
    num_meta = param.pop(0)
    meta_sum = 0
    for i in range(num_children):
        meta_sum += _sum_meta(param)

    for i in range(num_meta):
        meta_sum += param.pop(0)

    return meta_sum


if __name__ == "__main__":
    test_meta_sum = sum_meta("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
    assert test_meta_sum == 138, test_meta_sum

    c1 = challenge1()
    assert c1 == 49180

