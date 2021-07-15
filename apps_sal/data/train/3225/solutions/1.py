def find_all(array, n):
    res = []
    for i in range(len(array)):
        if array[i] == n:
            res.append(i)
    return res
