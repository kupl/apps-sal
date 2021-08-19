from bisect import bisect, bisect_left
from typing import List


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = []
        filled = {}
        free_day = []
        for (index, city) in enumerate(rains):
            if city:
                result.append(-1)
                if city not in filled:
                    filled[city] = index
                else:
                    if len(free_day) > 0 and free_day[-1] > filled[city]:
                        dry_day = bisect_left(free_day, filled[city])
                        result[free_day.pop(dry_day)] = city
                        filled[city] = index
                        pass
                    else:
                        return []
                    pass
                pass
            else:
                result.append(1)
                free_day.append(index)
                pass
            pass
        return result
