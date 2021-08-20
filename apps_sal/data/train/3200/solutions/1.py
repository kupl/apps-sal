import itertools as it


def thirt(n):
    if n < 100:
        return n
    pattern = it.cycle([1, 10, 9, 12, 3, 4])
    return thirt(sum((d * n for (d, n) in zip(list(map(int, str(n)[::-1])), pattern))))
