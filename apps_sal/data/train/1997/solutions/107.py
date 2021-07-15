class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # for each interval, check all other intervals to see if it is
        # covered by some other interval
        i = 0
        
        while (i < len(intervals)):
            current_int = intervals[i]
            
            # check all other intervals
            for j in range(i + 1, len(intervals)):
                int1 = intervals[j]
                
                # if current interval covers this interval or this
                # interval covers the current interval, remove the 
                # interval that is covered
                if (current_int[0] <= int1[0] and current_int[1] >= int1[1]):
                    intervals.remove(int1)
                    i -= 1
                    break
                elif (int1[0] <= current_int[0] and int1[1] >= current_int[1]):
                    intervals.remove(current_int)
                    i -= 1
                    break
            
            i += 1
        
        return len(intervals)

