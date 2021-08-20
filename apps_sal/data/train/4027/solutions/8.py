def sum_nested_numbers(arr, d=1):
    my_sum = 0
    for v in arr:
        if isinstance(v, list):
            my_sum += sum_nested_numbers(v, d + 1)
        else:
            my_sum += v ** d
    return my_sum
