def min_sum(arr):
    prods = []
    for i in range(len(arr) // 2):
        prods.append(max(arr) * min(arr))
        arr.remove(max(arr))
        arr.remove(min(arr))
    return sum(prods)
