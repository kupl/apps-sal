def first_n_smallest(arr, n):
    smallest = []
    replacement = max(arr) + 1
    while n and arr:
        num = min(arr)
        idx = arr.index(num)
        arr[idx] = replacement
        smallest.append((num, idx))
        n -= 1
    sort = sorted(smallest, key=lambda pair: pair[1])
    return [p[0] for p in sort]
