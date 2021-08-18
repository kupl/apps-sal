def shortest(N, edgeList):
    import math
    edgeList.sort(key=lambda x: x[0])
    path_length = [math.inf for _ in range(N)]
    path_length[0] = 0

    for start, end, weight in edgeList:
        if path_length[start] == math.inf:
            continue
        path_length[end] = min(path_length[start] + weight, path_length[end])

    result = path_length[N - 1]
    return result if result is not math.inf else -1
