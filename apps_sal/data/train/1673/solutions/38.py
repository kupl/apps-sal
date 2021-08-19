import heapq


class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        while len(arr) > 1:
            row = arr.pop()
            heap = []
            for i in range(len(row)):
                if not heap:
                    heap = [row[x] for x in range(len(row)) if x != i]
                    heapq.heapify(heap)
                else:
                    if heap[0] == row[i]:
                        heapq.heappop(heap)
                    heapq.heappush(heap, row[i - 1])
                arr[-1][i] += heap[0]
        return min(arr[0])
