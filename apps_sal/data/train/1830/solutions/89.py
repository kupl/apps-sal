class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full_lakes = {}
        
        sunny_days = []
        
        res = []
        
        for i, rain in enumerate(rains):
            if rain == 0:
                res.append(1)
                sunny_days.append(i)
            else:
                if rain in full_lakes:
                    last_rain = full_lakes[rain]
                    
                    earliest_sunny_day = -1
                    for day in sunny_days:
                        if day > last_rain and day < i:
                            earliest_sunny_day = day
                            sunny_days.remove(day)
                            break
                            
                    if earliest_sunny_day == -1:
                        return []
                    
                    res[earliest_sunny_day] = rain
                    res.append(-1)

                else:
                    res.append(-1)
                full_lakes[rain] = i
        return res
