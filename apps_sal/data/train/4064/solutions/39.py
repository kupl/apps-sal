def count_by(x, n):
    arr = [0]
    for i in range(n):
        arr.append(arr[-1] + x)
    return arr[1:]
