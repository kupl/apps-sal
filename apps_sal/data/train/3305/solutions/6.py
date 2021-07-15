def shortest(n, edges):
    m = [0] + [-1] * (n-1)
    for start, end, weight in sorted(edges):
        if m[start] == -1: continue
        m[end] = min(m[start] + weight,
                     m[end] == -1 and float('inf') or m[end])
    return m[-1]
