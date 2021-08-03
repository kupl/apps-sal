
"""

両方から距離Lの点の数がわかればよい
STからダイクストラ

頂点がなる場合→調べる
辺の間でなる場合
両方近いほうが異なる & その和+辺の長さが2L

ぶつかるものを引きたい
その頂点までの経路数も求めておく

"""

from sys import stdin

import heapq


def Dijkstra(lis, start):

    ret = [float("inf")] * len(lis)
    rnum = [0] * len(lis)
    rnum[start] = 1

    ret[start] = 0
    end_flag = [False] * len(lis)
    end_num = 0

    q = [[0, start]]

    while len(q) > 0:

        ncost, now = heapq.heappop(q)

        if end_flag[now]:
            continue

        end_flag[now] = True
        end_num += 1

        if end_num == len(lis):
            break

        for nex, ecost in lis[now]:

            if ret[nex] > ncost + ecost:
                ret[nex] = ncost + ecost
                heapq.heappush(q, [ret[nex], nex])
                rnum[nex] = 0
            if ret[nex] == ncost + ecost:
                rnum[nex] = (rnum[nex] + rnum[now]) % mod
        #print (now,rnum)
    return ret, rnum


N, M = list(map(int, stdin.readline().split()))
S, T = list(map(int, stdin.readline().split()))
S -= 1
T -= 1
mod = 10**9 + 7

lis = [[] for i in range(N)]
for i in range(M):
    u, v, d = list(map(int, stdin.readline().split()))
    u -= 1
    v -= 1
    lis[u].append((v, d))
    lis[v].append((u, d))

DS, rootS = Dijkstra(lis, S)
DT, rootT = Dijkstra(lis, T)

ans = (rootS[T] ** 2) % mod
L = DS[T]

#print (DS,rootS)

for v in range(N):

    if L % 2 == 0 and DS[v] == DT[v] == L // 2:
        ans -= (rootS[v] * rootT[v]) ** 2
        continue

    for nex, ecost in lis[v]:
        if nex < v:
            if DS[v] + DT[nex] + ecost == L and DS[v] * 2 < L and DT[nex] * 2 < L:
                ans -= (rootS[v] * rootT[nex]) ** 2
            elif DS[nex] + DT[v] + ecost == L and DS[nex] * 2 < L and DT[v] * 2 < L:
                ans -= (rootS[nex] * rootT[v]) ** 2
            ans %= mod

print((ans % mod))
