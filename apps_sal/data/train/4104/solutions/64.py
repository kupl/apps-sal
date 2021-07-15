def max_tri_sum(numbers):
    new_list = sorted(set(numbers))
    return sum(new_list[-3:])
