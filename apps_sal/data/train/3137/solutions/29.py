from math import ceil


def round_it(n):
    left = len(str(n).split(".")[0])
    right = len(str(n).split(".")[1])
    return int(n) if left > right else ceil(n) if left < right else round(n)
