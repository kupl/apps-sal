from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = float('inf')
MOD = 10**9 + 7

def Dijkstra(adjList, vSt):
    numV = len(adjList)
    numUsed = 0
    costs = [INF] * numV
    costs[vSt] = 0
    nums = [0] * numV
    nums[vSt] = 1
    PQ = []
    heappush(PQ, (0, vSt))
    while PQ:
        cNow, vNow = heappop(PQ)
        if cNow > costs[vNow]: continue
        numUsed += 1
        if numUsed == numV: break
        for v2, wt in adjList[vNow]:
            c2 = cNow + wt
            if c2 < costs[v2]:
                costs[v2] = c2
                nums[v2] = nums[vNow]
                heappush(PQ, (c2, v2))
            elif c2 == costs[v2]:
                nums[v2] = (nums[v2]+nums[vNow]) % MOD
    return (costs, nums)

def solve():
    N, M = list(map(int, input().split()))
    S, T = list(map(int, input().split()))
    S, T = S-1, T-1
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    adjL = [[] for _ in range(N)]
    for u, v, d in edges:
        adjL[u-1].append((v-1, d))
        adjL[v-1].append((u-1, d))

    costSs, numSs = Dijkstra(adjL, S)
    costTs, numTs = Dijkstra(adjL, T)
    minCost = costSs[T]

    ans = (numSs[T]**2) % MOD
    for v in range(N):
        if costSs[v] == costTs[v] == minCost/2:
            k = (numSs[v]*numTs[v]) % MOD
            ans -= (k**2) % MOD
            ans %= MOD
    for u, v, d in edges:
        u, v = u-1, v-1
        if costSs[u] > costSs[v]:
            u, v = v, u
        if costSs[u] < minCost/2 and costTs[v] < minCost/2 and costSs[u]+d+costTs[v] == minCost:
            k = (numSs[u]*numTs[v]) % MOD
            ans -= (k**2) % MOD
            ans %= MOD

    print(ans)

solve()

