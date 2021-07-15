import heapq
import math

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        starts = []
        ends = []
        
        for start, end in requests:
            heapq.heappush(starts, (start, end))
        
        curr_start = None
        new_ranges = []
        
        while len(starts) > 0:
            peek_start = starts[0]
            
            peek_end = ends[0] if len(ends) > 0 else (math.inf, math.inf)
            if peek_end[0] < peek_start[0]:
                new_ranges.append((curr_start, peek_end[0], len(ends)))
                while len(ends) > 0 and ends[0][0] == peek_end[0]:
                    heapq.heappop(ends)
                curr_start = peek_end[0] + 1
            elif peek_end[0] > peek_start[0]:
                if len(ends) > 0:
                    new_ranges.append((curr_start, peek_start[0] - 1, len(ends)))
                while len(starts) > 0 and starts[0][0] == peek_start[0]:
                    elt = heapq.heappop(starts) 
                    heapq.heappush(ends, (elt[1], elt[0]))
                curr_start = peek_start[0]
            else:
                new_ranges.append((curr_start, peek_end[0] - 1, len(ends)))
                
                while len(starts) > 0 and starts[0][0] == peek_start[0]:
                    elt = heapq.heappop(starts) 
                    heapq.heappush(ends, (elt[1], elt[0]))
                
                new_ranges.append((peek_end[0], peek_end[0], len(ends)))
                
                while len(ends) > 0 and ends[0][0] == peek_end[0]:
                    heapq.heappop(ends)  
                
                curr_start = peek_end[0] + 1
         
        while len(ends) > 0:
            peek_end = ends[0]
            new_ranges.append((curr_start, peek_end[0], len(ends)))
            while len(ends) > 0 and ends[0][0] == peek_end[0]:
                heapq.heappop(ends)
            curr_start = peek_end[0] + 1
           
        counts = [0] * len(nums)
        for start, end, f in new_ranges:
            for i in range(start, end + 1):
                counts[i] += f  
        sorted_indices = sorted(counts)
        sorted_elts = sorted(nums)
        

        res = 0
        while len(sorted_elts) > 0:
            res += sorted_elts.pop() * sorted_indices.pop()
        return res % (10 ** 9 + 7)
