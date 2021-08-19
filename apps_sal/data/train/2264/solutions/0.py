# ARC090E

def hoge():
    M = 10**9 + 7
    import sys
    def input(): return sys.stdin.readline().rstrip()

    n, m = map(int, input().split())
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    from collections import defaultdict
    ns = defaultdict(set)
    for i in range(m):
        u, v, d = map(int, input().split())
        ns[u - 1].add((v - 1, d))
        ns[v - 1].add((u - 1, d))

    def _dijkstra(N, s, Edge):
        import heapq
        geta = 10**15
        inf = geta
        dist = [inf] * N
        dist[s] = 0
        Q = [(0, s)]
        dp = [0] * N
        dp[s] = 1
        while Q:
            dn, vn = heapq.heappop(Q)
            if dn > dist[vn]:
                continue
            for vf, df in Edge[vn]:
                if dist[vn] + df < dist[vf]:
                    dist[vf] = dist[vn] + df
                    dp[vf] = dp[vn]
                    heapq.heappush(Q, (dn + df, vf))
                elif dist[vn] + df == dist[vf]:
                    dp[vf] = (dp[vf] + dp[vn]) % M
        return dist, dp

    def dijkstra(start):
        import heapq
        vals = [None] * n
        nums = [None] * n
        nums[start] = 1
        h = [(0, start)]  # (距離, ノード番号)
        vals[start] = 0
        while h:
            val, u = heapq.heappop(h)
            for v, d in ns[u]:
                if vals[v] is None or vals[v] > val + d:
                    vals[v] = val + d
                    nums[v] = nums[u]
                    heapq.heappush(h, (vals[v], v))
                elif vals[v] is not None and vals[v] == val + d:
                    nums[v] = (nums[v] + nums[u]) % M
        return vals, nums

    vals1, nums1 = dijkstra(s)
    vals2, nums2 = dijkstra(t)

    T = vals1[t]

    c1 = 0  # 頂点で衝突するペアの数
    c2 = 0  # エッジ(端点除く)で衝突するペアの数

    for u in range(n):
        if 2 * vals1[u] == T and 2 * vals2[u] == T:
            c1 = (c1 + pow((nums1[u] * nums2[u]), 2, M)) % M
        for v, d in ns[u]:
            if (vals1[u] + d + vals2[v] == T) and (2 * vals1[u] < T < 2 * (vals1[u] + d)):
                c2 = (c2 + (nums1[u] * nums2[v])**2) % M
    print((nums1[t] * nums2[s] - (c1 + c2)) % M)


hoge()
