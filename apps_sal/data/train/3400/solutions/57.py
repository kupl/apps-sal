def even_numbers(arr, n):
    res = []
    for ele in reversed(arr):
        if ele % 2 == 0:
            res.append(ele)
    return list(reversed(res[:n]))
