stirling2 = [[1]]


def combs_non_empty_boxes(n, k):
    for _ in range(len(stirling2), n + 1):
        stirling2.append([a + r * b for r, (a, b) in
                          enumerate(zip([0] + stirling2[-1], stirling2[-1] + [0]))])
    return stirling2[n][k] if k <= n else "It cannot be possible!"
