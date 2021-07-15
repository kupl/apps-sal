def max_product(arr, n):
    b = sorted(arr, reverse=True)
    acc = 1
    for i in b[:n]:
        acc *= i
    return acc
