from functools import cmp_to_key


def largest_arrangement(numbers):

    @cmp_to_key
    def cmp(a, b):
        return int(b + a) - int(a + b)

    return int(''.join(n for n in sorted(map(str, numbers), key=cmp)))
