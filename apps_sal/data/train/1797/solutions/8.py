def hamming(n):
    (h, i, j, k) = ([1] * n, 0, 0, 0)
    for nn in range(1, n):
        h[nn] = min(2 * h[i], 3 * h[j], 5 * h[k])
        i += 2 * h[i] == h[nn]
        j += 3 * h[j] == h[nn]
        k += 5 * h[k] == h[nn]
    return h[-1]
