class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cov = 0
        
        # First covers second?
        def covered(first,second):
            return (first[0] <= second[0]) and (second[1] <= first[1])
        
        for pos,inter1 in enumerate(intervals):
            for checkpos,inter2 in enumerate(intervals):
                # print(inter1, inter2)
                if pos != checkpos and covered(inter2,inter1): 
                    # print(\"covered\")
                    cov += 1
                    break
                    
        return len(intervals) - cov
