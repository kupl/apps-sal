class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # while len(stones) > 1:
        #     stones.sort()
        #     num = stones.pop() - stones.pop()
        #     stones.append(num)
        # return 0 if len(stones) == 0 else stones[0]
        
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1 and heap[0] != 0:
            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))
        return - heap[0]
