import string


def reduce_polymer_more(cur_input):
    min_length = len(cur_input)
    best_polymer = None
    for lower_c in string.ascii_lowercase:
        upper_c = chr(ord(lower_c) - 32)
        test_input = reduce_polymer(
            (cur_input + "")\
            .replace(lower_c, "")\
            .replace(upper_c, "")
        )
        if len(test_input) < min_length:
            best_polymer = test_input
            min_length = len(test_input)

    return reduce_polymer(best_polymer)


def reduce_polymer(cur_input):
    while True:
        starting_input = cur_input + ""
        reduced_something = False
        for lower_c in string.ascii_lowercase:
            upper_c = chr(ord(lower_c) - 32)
            cur_input = cur_input\
                .replace(lower_c + upper_c, '')\
                .replace(upper_c + lower_c, '')
            if len(starting_input) != len(cur_input):
                reduced_something = True

        if not reduced_something:
            return cur_input


def challenge1():
    with open("inputs/polymer.txt", "r") as fd:
        return reduce_polymer(fd.read().strip())


def challenge2():
    with open("inputs/polymer.txt", "r") as fd:
        return reduce_polymer_more(fd.read().strip())


if __name__ == "__main__":
    test = reduce_polymer("dabAcCaCBAcCcaDA")
    assert "dabCBAcaDA" == reduce_polymer("dabAcCaCBAcCcaDA"), test
    assert "daDA" == reduce_polymer_more("dabAcCaCBAcCcaDA"), test
    print(len(challenge1()))
    print(len(challenge2()))
