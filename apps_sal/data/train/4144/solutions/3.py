def abundant(limit):
    for n in range(limit, 0, -1):
        div_sum = sum(x for x in range(1, n//2 + 1) if n%x == 0)
        if div_sum > n:
            return [ [n], [div_sum - n] ]
