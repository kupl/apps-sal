from collections import Counter


def check_three_and_two(array):
    return sorted(Counter(array).values()) == [2, 3]
