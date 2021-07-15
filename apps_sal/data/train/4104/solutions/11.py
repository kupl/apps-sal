def max_tri_sum(numbers):
    sorted_set = list(set(sorted(numbers)))
    sorted_list = sorted(sorted_set)
    return sum(sorted_list[-3:])
