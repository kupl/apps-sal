def max_number(n):
    arr = sorted(list(str(n)))
    arr_int = [int(elem) for elem in arr][::-1]
    arr_str = [str(elem) for elem in arr_int]
    result = ''.join(arr_str)

    return int(result)
