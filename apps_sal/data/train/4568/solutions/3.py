def find_min_max_product(arr, k):
    if k > len(arr):
        return None
    arr.sort(key=abs, reverse=True)
    (neg, pos, prod) = (None, None, 1)
    for i in range(k):
        if arr[i] < 0:
            neg = arr[i]
        if arr[i] > 0:
            pos = arr[i]
        prod *= arr[i]
    (neg1, pos1) = (None, None)
    for i in range(k, len(arr)):
        if not neg1 and arr[i] < 0:
            neg1 = arr[i]
        if not pos1 and arr[i] > 0:
            pos1 = arr[i]
        if neg1 and pos1:
            break
    candidates = [prod]
    if neg and pos1:
        candidates.append(prod // neg * pos1)
    if pos and neg1:
        candidates.append(prod // pos * neg1)
    if not (neg and neg1 and pos and pos1):
        prod = 1
        for i in range(-k, 0):
            prod *= arr[i]
        candidates.append(prod)
    return (min(candidates), max(candidates))
