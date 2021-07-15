def even_numbers(arr, n):
    if not arr or n == 0:
        return []
    if arr[-1] % 2 == 0:
        v = n - 1
        tail = [arr[-1]]
    else:
        v = n
        tail = []
    return even_numbers(arr[:-1], v) + tail
