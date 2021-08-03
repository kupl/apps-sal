def max_tri_sum(numbers):
    # your code here
    z = set(numbers)
    x = sorted(z, reverse=True)
    return sum(x[0:3])
