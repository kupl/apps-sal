class Solution:
    class Union:
        def __init__(self):
            self.collection = {}

        def get_head(self, i):
            if i not in self.collection:
                return -1, 1
            while i in self.collection and self.collection[i][0] != i:
                i = self.collection[i][0]
            return self.collection[i]

        def add(self, i, j):
            head_i, cnt_i = self.get_head(i)
            head_j, cnt_j = self.get_head(j)

            if head_i == head_j and head_i != -1:
                return False

            head = head_i if cnt_i >= cnt_j else head_j
            cnt = cnt_i + cnt_j
            if head == -1:
                head = i

            self.collection[head_i] = (head, cnt)
            self.collection[head_j] = (head, cnt)
            self.collection[i] = (head, cnt)
            self.collection[j] = (head, cnt)
            return True

    from heapq import heappush, heappop

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        union = Solution.Union()
        total = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                val = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(heap, (val, i, j))

        while heap:
            val, i, j = heappop(heap)
            x = union.add(i, j)
            if x:
                total += val

        return total
