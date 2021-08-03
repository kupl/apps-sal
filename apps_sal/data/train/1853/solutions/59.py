class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = collections.defaultdict(list)
        res = [0] * n
        for a, b, d in edges:
            graph[a].append([b, d])
            graph[b].append([a, d])
        for i in range(n):
            queue = [[0, i]]
            visit = set()
            while queue:
                t, curr = heapq.heappop(queue)
                if t <= threshold and curr not in visit:
                    visit.add(curr)
                    for nei, dis in graph[curr]:
                        heapq.heappush(queue, [t + dis, nei])
            res[i] = len(visit) - 1
        return -sorted([[v, -i] for i, v in enumerate(res)])[0][1]
