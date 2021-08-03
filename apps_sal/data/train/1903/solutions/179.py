class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        union_find = dict()
        for i in range(len(points)):
            union_find[i] = i
            for j in range(i + 1, len(points)):
                heapq.heappush(heap, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))

        def find_set(node, ufo):
            if ufo[node] == node:
                return node
            else:
                return find_set(ufo[node], ufo)

        cost = 0
        n = 0
        while heap:
            currEdge = heapq.heappop(heap)
            left_root = find_set(currEdge[1], union_find)
            right_root = find_set(currEdge[2], union_find)
            if left_root != right_root:
                cost += currEdge[0]
                n += 1
                if n == (len(points) - 1):
                    break
                union_find[left_root] = right_root

        return cost
