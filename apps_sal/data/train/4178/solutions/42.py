def min_sum(arr):
    arr = sorted(arr)
    product = []
    for i in range(len(arr) // 2):
        product.append(arr[-i - 1] * arr[i])
    return sum(product)
