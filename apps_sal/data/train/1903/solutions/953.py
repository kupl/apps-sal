class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        visited = set()
        adj_list = defaultdict(list)
        cost = 0
        pq = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                first = points[i]
                second = points[j]
                adj_list[tuple(first)].append([abs(first[0] - second[0]) + abs(first[1] - second[1]), second])
                adj_list[tuple(second)].append([abs(first[0] - second[0]) + abs(first[1] - second[1]), first])

        pq = pq + adj_list[list(adj_list.keys())[0]]
        heapq.heapify(pq)
        visited.add(tuple(list(adj_list.keys())[0]))
        while len(visited) < len(adj_list):
            curr = heapq.heappop(pq)
            if tuple(curr[1]) not in visited:
                visited.add(tuple(curr[1]))
                for edge in adj_list[tuple(curr[1])]:
                    heapq.heappush(pq, edge)
                cost += curr[0]
        return cost
