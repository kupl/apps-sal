import heapq
import sys


def input():
    return sys.stdin.readline()[:-1]


MOD = 10**9 + 7


class DijkstraList():
    # 隣接リスト版
    # 同一頂点の複数回探索を防ぐため訪問した頂点数を変数cntで持つ
    def __init__(self, adj, start):
        self.list = adj
        self.start = start
        self.size = len(adj)

    def solve(self):
        self.dist = [float("inf") for _ in range(self.size)]
        self.dist[self.start] = 0
        self.dp = [0 for _ in range(self.size)]
        self.dp[self.start] = 1
        #self.prev = [-1 for _ in range(self.size)]
        self.q = []
        self.cnt = 0

        heapq.heappush(self.q, (0, self.start))

        while self.q and self.cnt < self.size:
            u_dist, u = heapq.heappop(self.q)
            if self.dist[u] < u_dist:
                continue
            for v, w in self.list[u]:
                if self.dist[v] > u_dist + w:
                    self.dist[v] = u_dist + w
                    self.dp[v] = self.dp[u]
                    #self.prev[v] = u
                    heapq.heappush(self.q, (self.dist[v], v))
                elif self.dist[v] == u_dist + w:
                    self.dp[v] += self.dp[u]
                    self.dp[v] %= MOD

            self.cnt += 1
        # print(self.dp)
        return

    def distance(self, goal):
        return self.dist[goal]

    def get_dp(self, x):
        return self.dp[x]


n, m = map(int, input().split())
s, t = map(int, input().split())
s, t = s - 1, t - 1
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v, d = map(int, input().split())
    adj[u - 1].append([v - 1, d])
    adj[v - 1].append([u - 1, d])
S, T = DijkstraList(adj, s), DijkstraList(adj, t)
S.solve()
T.solve()
ans = pow(S.get_dp(t), 2, MOD)
goal = S.distance(t)
#print(ans, goal)

for i in range(n):
    SI, TI = S.distance(i), T.distance(i)
    if SI + TI != goal:
        continue
    if SI * 2 == goal:
        ans -= S.get_dp(i) * T.get_dp(i) * S.get_dp(i) * T.get_dp(i)
        ans %= MOD

    else:
        for j, d in adj[i]:
            if i > j:
                continue
            SJ, TJ = S.distance(j), T.distance(j)
            if SJ + TJ != goal or abs(SI - SJ) != d:
                continue
            if SI * 2 < goal < SJ * 2:
                #print(i, j, SI, SJ)
                ans -= S.get_dp(i) * T.get_dp(j) * S.get_dp(i) * T.get_dp(j)
                ans %= MOD
            elif SJ * 2 < goal < SI * 2:
                #print(i, j, SI, SJ)
                ans -= S.get_dp(j) * T.get_dp(i) * S.get_dp(j) * T.get_dp(i)
                ans %= MOD

print(ans)
