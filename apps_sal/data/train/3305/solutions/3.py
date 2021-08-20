def shortest(N, edges):
    path = [0] + [float('inf')] * (N - 1)
    for (start, end, weight) in sorted(edges):
        if path[start] == -1:
            continue
        path[end] = min(path[start] + weight, path[end])
    return -1 if path[-1] == float('inf') else path[-1]
