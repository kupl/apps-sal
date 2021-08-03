def count_by(x, n):
    i = 0
    arr = [0] * n
    for i in range(n):
        arr[i] = x * (i + 1)
    return arr
