import sys


def resultSur97(x):
    return x % (10 ** 9 + 7)


def __starting_point():
    nl = list(map(int, input().split()))

    x = nl[0]
    sList = [input() for _ in range(x)]

    sListSorted = sorted(sList)
    out = ""
    for s in sListSorted:
        out += s

    print(("{}".format(out)))


__starting_point()
