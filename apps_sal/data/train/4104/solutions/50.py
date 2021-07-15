def max_tri_sum(numbers):
    num = sorted(set(numbers))
    return sum(num[-3:])
