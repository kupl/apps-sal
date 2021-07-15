def count_by(x, n):
    min = x
    arr = [x]
    for i in range(n-1):
        min += x
        arr.append(min)
    return arr

