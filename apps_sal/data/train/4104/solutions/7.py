def max_tri_sum(numbers):
    sorted_numbers = sorted(set(numbers), reverse = True)
    return sum(sorted_numbers[:3])

