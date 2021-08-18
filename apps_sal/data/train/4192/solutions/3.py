def pairwise(arr, n):
    a, i, j, pairs = sorted(arr), 0, len(arr) - 1, []
    while i < j:
        tot = a[i] + a[j]
        if tot == n:
            pairs.extend([a[i], a[j]])
            i, j = i + 1, j - 1
        elif tot < n:
            i += 1
        else:
            j -= 1
    pairs.sort()

    indices = []
    i, last = 0, None
    for x in pairs:
        i = (indices[-1] + 1) if x == last else 0
        indices.append(arr.index(x, i))
        last = x

    return sum(indices)
