def obtain_max_number(arr):
    last_len = 0
    while len(arr) != last_len:
        last_len = len(arr)
        for n in arr:
            if arr.count(n) > 1:
                arr.remove(n)
                arr.remove(n)
                arr.append(n * 2)

    return max(arr)
