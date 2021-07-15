class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        \"\"\"
            using deque canDry to store the possible days that can be used to dry a lake
            using hasRain to store the lake : day pairs
            update rules:
                1) if lake rains[i] rains on day i, check if it has rained before or not
                    if it has rained before, check if there is a way to dry it 
                        binary search the interval between two rain days
                    if there is no way to dry it, return []
                2) if there is no rain on day i, put i in canDry
        \"\"\"
        dry, res, rained = [], [], {}
        
        for i, lake in enumerate(rains):
            if lake > 0: # lake rains on day i
                res.append(-1)
                if lake in rained: # lake has rained before
                    idx = bisect.bisect(dry, rained[lake]) # search for the index of the 
                    if idx < len(dry): # a valid day is found to dry lake
                        day = dry[idx]
                        res[day] = lake
                        dry.pop(idx)
                        rained[lake] = i
                    else:
                        return []
                else: # lake has not rained before
                    rained[lake] = i
            else: # no rain on day i
                dry.append(i)
                res.append(0)
        
        for day in dry:
            res[day] = 1
        return res
       
