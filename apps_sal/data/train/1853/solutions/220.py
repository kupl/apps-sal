class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        G = collections.defaultdict(list)

        for e in edges:
            G[e[0]].append((e[1], e[2]))
            G[e[1]].append((e[0], e[2]))

        def dfs(i):
            dist = [math.inf] * n
            dist[i] = 0
            Queue = collections.deque([(i, 0)])

            while Queue:
                j, d = Queue.popleft()
                for k in G[j]:
                    if d + k[1] < dist[k[0]] and d + k[1] <= distanceThreshold:
                        dist[k[0]] = d + k[1]
                        Queue.append((k[0], d + k[1]))
            return sum(dist[i] < math.inf for i in range(n)) - 1

        nei = [(dfs(i), -i) for i in range(n)]
        heapq.heapify(nei)
        ans = heapq.heappop(nei)
        return -ans[1]
