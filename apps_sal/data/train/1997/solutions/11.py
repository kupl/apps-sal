class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
         # n log n time
        intervals.sort(reverse = True)
        intervals.sort(key = lambda i: i[1])
        
        covered = set() # n space
        
        for i, (c, d) in enumerate(intervals):
            for (a, b) in intervals[0: i]:
                #print((a,b), (c,d), c <= a, b <= d)
                
                if  c <= a and b <= d:
                    #print(\"covered\")
                    covered.add((a, b))
                    
        #print(covered)
        return len(intervals) - len(covered)
