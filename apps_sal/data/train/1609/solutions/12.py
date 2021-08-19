from bisect import bisect


def sum_of_intervals(intervals):
    I = []
    for (a, b) in intervals:
        i = bisect(I, a)
        j = bisect(I, b)
        I = I[:i] + [a] * (1 - i % 2) + [b] * (1 - j % 2) + I[j:]
    return sum(I[1::2]) - sum(I[::2])
