def find_longest(arr):
    max_digits = arr[0]   
    for i in range(1, len(arr)):
        if len(str(arr[i])) > len(str(max_digits)):
            max_digits = arr[i]
    return max_digits
