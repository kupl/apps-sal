def max_tri_sum(numbers):
    return sum(i for i in sorted(set(numbers))[-3:])
