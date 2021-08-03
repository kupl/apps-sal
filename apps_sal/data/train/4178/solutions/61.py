def min_sum(arr):
    m = []
    while len(arr) > 0:
        m.append(max(arr) * min(arr))
        arr.remove(max(arr))
        arr.remove(min(arr))
    return sum(m)
