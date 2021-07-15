class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        
        trips.sort(key = lambda x: x[1])
        heap = []
        cur = 0
        
        for pas, start, end in trips:
            
            while heap and heap[0][0] <= start:
                cur -= heappop(heap)[1]
            
            heappush(heap, (end, pas))
            cur += pas
            if cur > capacity:
                return False
        return True

