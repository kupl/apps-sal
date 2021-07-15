class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        toremove = set()
        for i in range(0, len(intervals)-1):
            for j in range(i+1, len(intervals)):
                s1, e1 = intervals[i]
                s2, e2 = intervals[j]
                
                if s1>=s2 and e1<=e2:
                    toremove.add(i)
                elif s2>=s1 and e2<=e1:
                    toremove.add(j)
        
        # res = []
        # for i, interval in enumerate(intervals):
        #     if i in toremove:
        #         continue
        #     res.append(interval)
        
        return len(intervals) - len(toremove)
                

