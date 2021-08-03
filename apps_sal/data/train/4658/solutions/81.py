def max_product(arr, n):
    prod = 1
    arr = list(sorted(arr, reverse=True))
    for i in range(n):
        prod *= arr[i]
    return prod
