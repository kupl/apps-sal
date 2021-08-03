import itertools


def find_mult_3(num):
    total = 0
    _max = float("-inf")

    for lst in get_combos(num):
        for i in lst:
            if i[0] != "0":
                number = int("".join(i))
                if number % 3 == 0:
                    total += 1
                    if number > _max:
                        _max = number
    return [total, _max]


def get_combos(num):
    return [set(itertools.permutations(str(num), i)) for i in range(1, len(str(num)) + 1)]
