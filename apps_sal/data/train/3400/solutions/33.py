def even_numbers(arr, n):
    res = []

    for elem in arr[::-1]:
        if elem % 2 == 0:
            res.insert(0, elem)
            if len(res) == n:
                break

    return res
