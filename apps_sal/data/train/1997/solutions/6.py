class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort based on [smallest start time, largest end time): O(n*log(n))
        # Sliding window upto the next start that is larger than current end
        # If they overlap then discard.
        
        ordered_intervals = sorted(intervals, key=lambda x: (x[0],-x[1]))
        candidates = set()
        for i in range(len(intervals)):
            
            curr_start, curr_end = ordered_intervals[i]
            
            for j in range(i+1, len(intervals)):
            
                next_start, next_end = ordered_intervals[j]
                if next_start >= curr_end:
                    break
                    
                if next_end <= curr_end:
                    candidates.add(j)
                    
        #result = []
        #for i, interval in enumerate(ordered_intervals):
        #    if i not in candidates:
        #        result.append(interval)
        return len(intervals) - len(candidates)
                
                

