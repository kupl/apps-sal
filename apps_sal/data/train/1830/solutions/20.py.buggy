\"\"\"
[1,2,3,4]
rain[i] = 0 -> 抽水日
    dryDay.insert(i)
rain[i] = x
1) x is empty: fill[x] = i
2) x is full: when to drain x?
    must be in dryDays
    must be later than fill[x]
    
      1  2  3  4  5  6
fill  x     y     x 
dryD     -     x 


\"\"\"



class Solution:
    def avoidFlood(self, rains):
        filled = {}
        dryDays = []
        res = [1] * len(rains)

        for day, lake in enumerate(rains):
            if not lake:
                dryDays.append(day)
                continue 

            res[day] = -1
            if lake in filled:
                if not dryDays: return []
                # use the first dry day after the lake was filled (stored in filled[lake])
                idx = bisect.bisect_left(dryDays, filled[lake])
                if idx >= len(dryDays): 
                    return []
                dry_on_day = dryDays.pop(idx)
                res[dry_on_day] = lake

            filled[lake] = day # we fill it on day

        return res
        
        
        
        
        
