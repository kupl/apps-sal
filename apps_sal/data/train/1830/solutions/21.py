class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = []
        free_day = []
        filled = {}
        for (day, city) in enumerate(rains):
            if city:
                res.append(-1)
                if city not in filled:
                    filled[city] = day
                elif free_day and free_day[-1] > filled[city]:
                    dry_day = bisect.bisect_left(free_day, filled[city])
                    res[free_day.pop(dry_day)] = city
                    filled[city] = day
                else:
                    return []
            else:
                res.append(1)
                free_day.append(day)
        return res
