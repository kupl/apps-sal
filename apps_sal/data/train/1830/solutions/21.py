class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        res = []
        free_day = [] # days without rain
        filled = {}   # map of cities that are full (but not flooded) -> day that they were filled

        for day,city in enumerate(rains):
            if city: 
                res.append(-1)
                if city not in filled:                                       # 1
                    filled[city] = day                                       # 1
                else:
                    if free_day and (free_day[-1] > filled[city]):           # 3.1
                        dry_day = bisect.bisect_left(free_day, filled[city]) # 3.3
                        res[free_day.pop(dry_day)] = city                    # 3.3
                        filled[city] = day                                   # 3.3
                    else:
                        return []                                            # 3.2
            else:
                res.append(1)                                                # 2 (we will fill in rain free days later ~ use city 1 as a place holder)
                free_day.append(day)                                         # 2

        return res
                        

