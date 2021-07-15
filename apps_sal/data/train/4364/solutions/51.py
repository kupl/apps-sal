def odd_or_even(arr):
    arr_num = 0
    for i in arr:
        arr_num = arr_num + i
    return "odd" if arr_num % 2 != 0 else "even"

