def even_numbers(arr, n):
    evens_arr = [x for x in arr if x % 2 == 0]
    return evens_arr[len(evens_arr) - n:]
