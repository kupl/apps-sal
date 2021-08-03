from string import ascii_lowercase as ref


def solve(arr):
    return [sum([x.lower()[i] == ref[i] for i in range(min(26, len(x)))]) for x in arr]
