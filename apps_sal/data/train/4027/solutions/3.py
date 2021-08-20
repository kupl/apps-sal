def sum_nested_numbers(arr, depth=1):
    return sum((sum_nested_numbers(x, depth + 1) if type(x) is list else x ** depth for x in arr))
