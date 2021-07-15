class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dis2 = x**2 + y**2
            if len(heap)<K:
                heapq.heappush(heap, (-dis2, (x,y)))
            else:
                if -dis2>heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-dis2,(x,y)))
        ans = []
        for i in range(K):
            x,y = heapq.heappop(heap)[1]
            # ans = [[x, y]] + ans
            ans.append([x,y])
        return ans[::-1]
