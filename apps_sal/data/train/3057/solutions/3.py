def is_bouncy(n):
    lst = list(map(int, str(n)))
    return {1, -1} <= {(b < a) - (b > a) for (a, b) in zip(lst, lst[1:])}
