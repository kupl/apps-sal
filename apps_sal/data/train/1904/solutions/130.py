class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (a, b) in points:
            if len(heap) < K:
                heapq.heappush(heap, (-1 * (a ** 2 + b ** 2), [a, b]))
            else:
                heapq.heappushpop(heap, (-1 * (a ** 2 + b ** 2), [a, b]))
        op = []
        print(heap)
        for i in range(K):
            print(i)
            op.append(heap[i][1])
        return op
