class Solution:

    def minCostConnectPoints(self, points):
        n = len(points)
        graph = [[] for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append([j, dist])
                graph[j].append([i, dist])
        return mst(n, graph)


def mst(n, graph):
    keyval = [2 ** 31 - 1] * n
    keyval[0] = 0
    mst = [False] * n
    for i in range(n):
        u = minVal(keyval, mst)
        mst[u] = True
        for node in graph[u]:
            if mst[node[0]] == False and keyval[node[0]] > node[1]:
                keyval[node[0]] = node[1]
    return sum(keyval[1:])


def minVal(keyval, mst):
    minv = 2 ** 31 - 1
    minInd = 0
    for i in range(1, len(keyval)):
        if minv > keyval[i] and mst[i] == False:
            minv = keyval[i]
            minInd = i
    return minInd
