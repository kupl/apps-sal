def pairwise(arr, n):
    # fiond each pair of elements that add up to n in arr
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

    # Identify the lowest possible index for each element in pairs
    indices = []
    i, last = 0, None
    for x in pairs:
        # Continue from last found if repeat value else from start of array
        i = (indices[-1] + 1) if x == last else 0
        indices.append(arr.index(x, i))
        last = x

    return sum(indices)
