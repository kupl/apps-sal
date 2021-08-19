def faro_cycles(deck_size):
    (arr, count) = (list(range(deck_size)), 0)
    original_arr = arr
    while True:
        arr = arr[0:deck_size:2] + arr[1:deck_size:2]
        count += 1
        if original_arr == arr:
            break
    return count
