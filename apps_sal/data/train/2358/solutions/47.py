import heapq


def dijkstra_heap(N, s, edge):
    d = [float('inf')] * N
    used = [False] * N
    d[s] = 0
    used[s] = True
    edgelist = []
    for (v, w) in enumerate(edge[s]):
        heapq.heappush(edgelist, (w, v))
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        v = minedge[1]
        if used[v]:
            continue
        d[v] = minedge[0]
        used[v] = True
        for (u, w) in enumerate(edge[v]):
            if not used[u]:
                heapq.heappush(edgelist, (d[v] + w, u))
    return d


(A, B, C, D) = map(int, input().split())
N = int(input())
d = [[0] * (N + 2) for _ in range(N + 2)]
X = [0] * N
Y = [0] * N
R = [0] * N
for i in range(N):
    (X[i], Y[i], R[i]) = map(int, input().split())
d[0][-1] = ((C - A) ** 2 + (D - B) ** 2) ** 0.5
d[-1][0] = ((C - A) ** 2 + (D - B) ** 2) ** 0.5
for i in range(1, N + 1):
    d_s = max(0, ((X[i - 1] - A) ** 2 + (Y[i - 1] - B) ** 2) ** 0.5 - R[i - 1])
    d_e = max(0, ((X[i - 1] - C) ** 2 + (Y[i - 1] - D) ** 2) ** 0.5 - R[i - 1])
    (d[0][i], d[i][0]) = (d_s, d_s)
    (d[N + 1][i], d[i][N + 1]) = (d_e, d_e)
    for j in range(1, N + 1):
        d[i][j] = max(((X[i - 1] - X[j - 1]) ** 2 + (Y[i - 1] - Y[j - 1]) ** 2) ** 0.5 - R[i - 1] - R[j - 1], 0)
s = 0
d = dijkstra_heap(N + 2, s, d)
print(d[-1])
