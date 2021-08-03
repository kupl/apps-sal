from math import sqrt


def isPP(n):
    cur = int(sqrt(n)), 2
    while True:
        val = cur[0] ** cur[1]
        if val == 1:
            break
        if val > n:
            cur = cur[0] - 1, cur[1]
        elif val < n:
            cur = cur[0], cur[1] + 1
        else:
            return list(cur)
