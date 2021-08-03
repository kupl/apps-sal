class Solution:
    class Union:
        def __init__(self, n):
            self.collection = [(i, 1) for i in range(n)]
            self.max_cnt = 0
            self.size = n

        def get_head(self, i):
            if self.collection[i][0] != i:
                return self.get_head(self.collection[i][0])
            return self.collection[i]

        def add(self, i, j):
            head_i, cnt_i = self.get_head(i)
            head_j, cnt_j = self.get_head(j)
            if head_i == head_j:
                return False, self.max_cnt == self.size

            head = head_i if cnt_i >= cnt_j else head_j
            cnt = cnt_i + cnt_j

            for x in [head_i, head_j, i, j]:
                self.collection[x] = (head, cnt)

            self.max_cnt = max(self.max_cnt, cnt)
            return True, self.max_cnt == self.size

    from heapq import heappush, heappop

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        union = Solution.Union(len(points))
        total = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                val = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(heap, (val, i, j))

        while heap:
            val, i, j = heappop(heap)
            x, y = union.add(i, j)
            if x:
                total += val
            if y:
                break

        return total
