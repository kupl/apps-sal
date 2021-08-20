import string


def solve(arr: list):
    arr = list(map(str.lower, arr))
    same = []
    for s in arr:
        same.append(0)
        for (a, b) in zip(string.ascii_lowercase, s):
            same[-1] += a == b
    return same
