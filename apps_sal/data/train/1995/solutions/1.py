class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from collections import defaultdict
        
        log = defaultdict(int)
        
        for num, start, end in trips:
            log[start] += num
            log[end] -= num
        
        on_bus = 0
        for stop in sorted(log.keys()):
            on_bus += log[stop]
            if on_bus > capacity:
                return False
        
        return True
