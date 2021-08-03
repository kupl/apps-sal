def even_numbers(arr, n):
    arr = arr[::-1]
    number = []
    for x in range(len(arr)):
        if arr[x] % 2 == 0:
            if len(number) < n:
                number.append(arr[x])
            else:
                break
    return number[::-1]
