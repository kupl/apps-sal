class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        count = 0
        for i, [left, right] in enumerate(intervals):
            flag = True
            for j, [oleft, oright] in enumerate(intervals):
                if oleft <= left and right <= oright and i != j:
                    flag = False
                    continue
            if flag:
                count += 1
                
        
        return count
