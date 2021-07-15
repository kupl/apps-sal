def max_tri_sum(n):
    lst = sorted(set(n))[-3:]
    return sum([int(i) for i in lst])

