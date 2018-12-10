def challenge1():
    with open("inputs/license.txt", "r") as fd:
        return sum_meta(fd.read())


def challenge2():
    with open("inputs/license.txt", "r") as fd:
        return root_node_value(fd.read())


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


def root_node_value(param):
    param = list(map(int, param.split(" ")))
    return _root_node_value(param)


def _root_node_value(param):
    num_children = param.pop(0)
    num_meta = param.pop(0)
    child_values = []
    for i in range(num_children):
        child_values.append(_root_node_value(param))

    if num_children == 0:
        meta_sum = 0
        for i in range(num_meta):
            meta_sum += param.pop(0)
        return meta_sum
    else:
        node_value = 0
        for i in range(num_meta):
            meta = param.pop(0)
            if meta <= len(child_values):
                node_value += child_values[meta - 1]
        return node_value


if __name__ == "__main__":
    test_meta_sum = sum_meta("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
    assert test_meta_sum == 138, test_meta_sum

    c1 = challenge1()
    assert c1 == 49180

    test_node_value = root_node_value("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
    assert test_node_value == 66, test_node_value

    c2 = challenge2()
    assert c2 == 20611
