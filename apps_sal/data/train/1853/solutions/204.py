class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        G = [[] for _ in range(n)]

        for u, v, w in edges:
            G[u].append((v, w))
            G[v].append((u, w))

        cnt = [0] * n

        for i in range(n):
            dist = [10**18] * n
            dist[i] = 0
            pq = [(dist[i], i)]

            while pq:
                d, v = heappop(pq)

                if dist[v] < d:
                    continue

                for nv, w in G[v]:
                    if dist[nv] > dist[v] + w:
                        dist[nv] = dist[v] + w
                        heappush(pq, (dist[nv], nv))

            for j in range(n):
                if dist[j] <= distanceThreshold:
                    cnt[i] += 1

        M = 10**18

        for i in range(n):
            if M >= cnt[i]:
                M = cnt[i]
                ans = i

        return ans
