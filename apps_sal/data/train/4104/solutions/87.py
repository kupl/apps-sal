def max_tri_sum(n):
    n = list(set(n))
    n.sort(reverse=True)
    return sum(n[0:3])
