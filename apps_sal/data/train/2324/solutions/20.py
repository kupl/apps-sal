import heapq
import sys
input = sys.stdin.readline


def dijlstra_heap(N, s, edge):
    d = [float('inf')] * N
    used = [True] * N
    d[s] = 0
    edgelist = []
    for (a, b) in edge[s]:
        heapq.heappush(edgelist, a * 10 ** 6 + b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if not used[minedge % 10 ** 6]:
            continue
        v = minedge % 10 ** 6
        d[v] = minedge // 10 ** 6
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist, (e[0] + d[v]) * 10 ** 6 + e[1])
    return d


def main():
    N = int(input())
    edge = [[] for i in range(N)]
    for i in range(N - 1):
        (a, b) = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append([1, b])
        edge[b].append([1, a])
    d0 = dijlstra_heap(N, 0, edge)
    dn = dijlstra_heap(N, N - 1, edge)
    f_cnt = 0
    s_cnt = 0
    for i in range(N):
        if d0[i] <= dn[i]:
            f_cnt += 1
        else:
            s_cnt += 1
    if f_cnt > s_cnt:
        print('Fennec')
    else:
        print('Snuke')


def __starting_point():
    main()


__starting_point()
