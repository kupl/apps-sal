from queue import PriorityQueue
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        if not arr or len(arr) < 1:
            return []
        
        if len(arr) == 1:
            return arr
                    
        arr.sort()
        heap = []
        median = arr[(len(arr)-1)//2]
        
        
        for x in arr:
            heapq.heappush(heap,(abs(x-median), x))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [heapq.heappop(heap)[1] for _ in range(k)]

