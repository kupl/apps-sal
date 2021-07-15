class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = set()
        p1 = 0
        
        while p1 < len(intervals):
            if p1 in covered:
                p1 +=1
                continue
            p2 = p1 + 1
            while p2 <  len(intervals):
                if intervals[p1][0] <= intervals[p2][0] and intervals[p2][1] <= intervals[p1][1]:
                    covered.add(p2)
                elif intervals[p2][0] <= intervals[p1][0] and intervals[p1][1] <= intervals[p2][1]:
                    covered.add(p1)
                p2 += 1
            p1 += 1
                
        return len(intervals) - len(covered)
        

