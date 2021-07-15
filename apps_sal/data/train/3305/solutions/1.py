def shortest(n, edges):
    m = [0] + [float('inf')] * (n-1)
    for start, end, weight in sorted(edges):
        if m[start] == float('inf'): continue
        m[end] = min(m[start] + weight, m[end])
    return -1 if m[-1] == float('inf') else m[-1]
