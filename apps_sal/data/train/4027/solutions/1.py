def sum_nested_numbers(arr, m=1):
    total = 0
    for element in arr:
        if isinstance(element, int):
            total += element ** m
        else:
            total += sum_nested_numbers(element, m + 1)
    return total
