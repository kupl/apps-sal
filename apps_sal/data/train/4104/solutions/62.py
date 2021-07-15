def max_tri_sum(numbers):
    a = sorted(set((numbers)))
    return sum(a[-3::1])
