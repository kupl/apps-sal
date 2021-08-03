from heapq import heappush, heappop


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf')] * n for _ in range(n)]
        nei = collections.defaultdict(list)
        for i, j, x in edges:
            dis[i][j] = dis[j][i] = x
            nei[i].append(j)
            nei[j].append(i)
        for i in range(n):
            dis[i][i] = 0

        # Dijkstra
        visited = set()
        for i in range(n):
            pool = [(0, i)]                                          # pool[j] = x:  d(i,j) = x
            while pool:
                x, j = heappop(pool)                                 # x = d(i,j)
                if (i, j) not in visited and x <= distanceThreshold:  # early stop, if distance exceeds threshold
                    visited.add((i, j))
                    for k in nei[j]:
                        dis[i][k] = min(dis[i][k], x + dis[j][k])     # dis(i,k) = min(dis(i,k), dis(i,j)+dis(j,k))
                        heappush(pool, (dis[i][k], k))

        cities = {sum(d <= distanceThreshold for d in dis[i]): i for i in range(n)}
        print(cities)
        return cities[min(cities)]
