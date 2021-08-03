def shortest(N, edgeList):
    import math
    edgeList.sort(key=lambda x: x[0])
    path_length = [math.inf for _ in range(N)]
    path_length[0] = 0

    for start, end, weight in edgeList:
        #         each edge is written as [start, end, weight] where from < to więc to działa,
        #         ale gdyby taki warunek nie był prawdziwy to np.
        #         shortest(5, [(0,2,0), (0,3,1), (2,1,0), (3,4,1), (1,4,0)]) zwracałoby 2, zamiast 0
        if path_length[start] == math.inf:
            continue
        path_length[end] = min(path_length[start] + weight, path_length[end])

    result = path_length[N - 1]
    return result if result is not math.inf else -1


# def shortest(N, edgeList):
#     import math, heapq, collections
#     edges = collections.defaultdict(lambda:collections.defaultdict(lambda:math.inf))
#     path_length = [math.inf for _ in range(N)]
#     path_length[0] = 0
#     for start, end, weight in edgeList:
#         edges[start][end] = min(weight, edges[start][end])
#     h = [(0,0)]
#     visited = set()
#     heapq.heapify(h)
#     while h:
#         sum, start = heapq.heappop(h)
#         if start == N-1: return sum
#         if start in visited: continue
#         for end, weight in edges[start].items():
#             if end in visited: continue
#             if sum + weight < path_length[end]:
#                 path_length[end] = sum + weight
#                 heapq.heappush(h, (sum+weight, end))
#         visited.add(start)
#     return -1
