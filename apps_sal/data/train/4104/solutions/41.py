def max_tri_sum(num):
    return sum(sorted(set(num), reverse=True)[:3])
