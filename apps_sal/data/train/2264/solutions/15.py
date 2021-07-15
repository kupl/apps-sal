import sys
readline = sys.stdin.readline

from heapq import heappop as hpp, heappush as hp
def dijkstra(N, s, Edge):
    inf = geta
    dist = [inf] * N
    dist[s] = 0
    Q = [(0, s)]
    dp = [0]*N
    dp[s] = 1
    while Q:
        dn, vn = hpp(Q)
        if dn > dist[vn]:
            continue
        for df, vf in Edge[vn]:
            if dist[vn] + df < dist[vf]:
                dist[vf] = dist[vn] + df
                dp[vf] = dp[vn]
                hp(Q, (dn + df,vf))
            elif dist[vn] + df == dist[vf]:
                dp[vf] = (dp[vf] + dp[vn]) % MOD
    return dist, dp

MOD = 10**9+7
N, M = map(int, readline().split())
S, T = map(int, readline().split())
S -= 1
T -= 1

geta = 10**15
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v, d = map(int, readline().split())
    u -= 1
    v -= 1
    Edge[u].append((d, v))
    Edge[v].append((d, u))
    

dists, dps = dijkstra(N, S, Edge)
distt, dpt = dijkstra(N, T, Edge)
st = dists[T]

onpath = [i for i in range(N) if dists[i] + distt[i] == st]

ans = dps[T]**2%MOD
for i in onpath:
    if 2*dists[i] == 2*distt[i] == st:
        ans = (ans - pow(dps[i]*dpt[i], 2, MOD))%MOD
    
    for cost,vf in Edge[i]:
        if dists[i]+cost+distt[vf] == st:
            if 2*dists[i] < st < 2*dists[vf]:
                ans = (ans - pow(dps[i]*dpt[vf], 2, MOD))%MOD
print(ans)
