from sortedcontainers import SortedSet 

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        could_dry = SortedSet()
        last_rain = {}
        dry = {}
        for idx, rain in enumerate(rains):
            if rain == 0:
                could_dry.add(idx)
            else:
                if rain not in last_rain:
                    last_rain[rain] = idx
                else:  # need to find a dry
                    i = could_dry.bisect_left(last_rain[rain])
                    if i == len(could_dry):
                        return []  # could not find a good dry day
                    else:
                        day = could_dry[i]
                        dry[day] = rain
                        could_dry.remove(day)
                    last_rain[rain] = idx
        res = []
        for idx, rain in enumerate(rains):
            if rain == 0:
                res.append(dry.get(idx, 1))
            else:
                res.append(-1)
        return res
            

