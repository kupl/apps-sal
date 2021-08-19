def max_tri_sum(a):
    return sum(sorted(list(set(a)))[-3:])
