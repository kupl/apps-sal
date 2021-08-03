import heapq


Graph = []
N = 0


def dijkstras():
    Q = []
    visitedCount = [0] * N
    dist = [float("inf")] * N
    heapq.heappush(Q, tuple([0, 0]))
    dist[0] = 0
    visitedCount[0] = 1
    while len(Q) > 0:
        curDist, curNode = heapq.heappop(Q)
        for (nextNode, weight) in Graph[curNode]:
            nextDist = curDist + weight
            if nextDist == dist[nextNode]:
                visitedCount[nextNode] += visitedCount[curNode]
            elif nextDist < dist[nextNode]:
                visitedCount[nextNode] = visitedCount[curNode]
                dist[nextNode] = nextDist
                heapq.heappush(Q, (nextDist, nextNode))

    return visitedCount[N - 1]


def main():
    nonlocal N
    nonlocal Graph
    T = int(input())
    for test in range(T):
        N, M = tuple(map(int, input().split()))
        Graph = []
        for x in range(N):
            Graph.append([])
        for edge in range(M):
            Ai, Bi, Ci = tuple(map(int, input().split()))
            Graph[Ai - 1].append((Bi - 1, Ci))
            Graph[Bi - 1].append((Ai - 1, Ci))

        print(dijkstras())


def __starting_point():
    main()


__starting_point()
