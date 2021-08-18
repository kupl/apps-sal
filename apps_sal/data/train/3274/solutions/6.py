import math


def prefix_suffix_check(string, indexIn):
    return string[:indexIn] == string[(indexIn) * -1:]


def solve(initial_string):

    half_array_size = int(math.floor(len(initial_string) / 2))

    for x in range(half_array_size, 0, -1):
        if (prefix_suffix_check(initial_string, x) == True):
            return x

    return 0
