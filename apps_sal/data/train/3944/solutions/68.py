def sum_triangular_numbers(n):
    r = [0]
    [r.append(r[-1]+x) for x in range(n+1)]
    return sum(r)
