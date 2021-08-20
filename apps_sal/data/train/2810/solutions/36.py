from string import ascii_lowercase as letters


def solve(arr):
    return [sum((1 for (i, c) in enumerate(s) if i == letters.index(c.lower()))) for s in arr]
