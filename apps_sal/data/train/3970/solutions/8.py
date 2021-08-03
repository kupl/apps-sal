def odd_row(n):
    arr = []
    value = (n * n) - (n - 1)
    for i in range(n):
        arr.append(value)
        value += 2
    return arr
