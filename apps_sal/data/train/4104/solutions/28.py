def max_tri_sum(numbers):
    a=sorted(set(numbers),reverse=True)
    return sum(a[:3])
