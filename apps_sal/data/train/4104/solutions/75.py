def max_tri_sum(numbers):
    return sum([number for number in sorted(list(set(numbers)))[-1:-4:-1]])
