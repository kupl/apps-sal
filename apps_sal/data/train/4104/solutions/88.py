def max_tri_sum(numbers):
    numbers = set(numbers)
    return sum(sorted(numbers)[-3:])
