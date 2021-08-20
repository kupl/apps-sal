def update_if_new(d, results, element):
    if element not in d:
        results.append(element)
        d[element] = True


def merge_arrays(first, second):
    seen = dict()
    results = []
    (i, j, m, n) = (0, 0, len(first), len(second))
    while i < m and j < n:
        (x, y) = (first[i], second[j])
        if x < y:
            update_if_new(seen, results, x)
            i += 1
        else:
            update_if_new(seen, results, y)
            j += 1
    for residual in first[i:] + second[j:]:
        update_if_new(seen, results, residual)
    return results
