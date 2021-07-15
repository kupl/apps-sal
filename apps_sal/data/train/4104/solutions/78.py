def max_tri_sum(numbers):
    new_list = set(numbers)
    third_new_list = sorted(new_list, reverse=True )[:3]
    return (sum(third_new_list))
