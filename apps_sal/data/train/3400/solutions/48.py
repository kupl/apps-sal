def even_numbers(arr,n):
    c = 0
    res = []
    for i in range(len(arr)-1, -1, -1):
        if c == n:
            break
        elif arr[i] % 2 == 0:
            res.append(arr[i])
            c += 1
    return res[::-1]
