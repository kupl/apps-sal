def array_leaders(num):
    return [n for (i, n) in enumerate(num, 1) if n > sum(num[i:])]
