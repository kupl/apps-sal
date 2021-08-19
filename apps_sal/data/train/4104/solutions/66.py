def max_tri_sum(numbers):
    test_list = list(set(numbers))
    sorted_list = sorted(test_list)
    return sum(sorted_list[-3:])
