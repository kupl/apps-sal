def geometric_sequence_elements(a, r, n):
    arr = [a]
    for i in range(n - 1):
        arr.append(arr[i] * r)
    return ', '.join(map(str, arr))
