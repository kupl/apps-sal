from math import ceil


def infected_zeroes(li):
    zeros = [i for (i, j) in enumerate(li) if not j]
    l = [ceil((zeros[i + 1] - j - 1) / 2) for (i, j) in enumerate(zeros[:-1])]
    return max([zeros[0], len(li) - zeros[-1] - 1] + l)
