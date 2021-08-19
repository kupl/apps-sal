from collections import deque


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        ret = [-1 for i in range(0, len(rains))]
        filled_lakes = dict()
        dry_days = list()
        i = 0
        while i < len(rains):
            rain = rains[i]
            if rain == 0:
                dry_days.append(i)
            if rain > 0 and rain in filled_lakes:
                prev_pos = filled_lakes[rain]
                if len(dry_days) == 0:
                    return []
                j = 0
                while j < len(dry_days) and prev_pos > dry_days[j]:
                    j += 1
                if j == len(dry_days):
                    return []
                k = dry_days.pop(j)
                ret[k] = rain
            if rain != 0:
                filled_lakes[rain] = i
            i += 1
        while len(dry_days) > 0:
            j = dry_days.pop()
            ret[j] = 1
        return ret
