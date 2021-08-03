def max_tri_sum(numbers):
    num = sorted(list(set(numbers)))
    return sum(num[len(num) - 3:])
