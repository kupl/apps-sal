def round_to_next5(n):
    n = list(range(n, n + 5))
    res = [str(i) for i in n if i % 5 == 0]
    return int(''.join(res))
