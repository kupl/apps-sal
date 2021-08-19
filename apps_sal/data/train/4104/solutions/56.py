def max_tri_sum(numbers):
    z = set(numbers)
    x = sorted(z, reverse=True)
    return sum(x[0:3])
