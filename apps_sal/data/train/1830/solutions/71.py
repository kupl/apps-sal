from collections import defaultdict


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry_days = []
        filled_lakes = {}
        ans = [1] * len(rains)
        for i in range(len(rains)):
            if rains[i] != 0:
                ans[i] = -1
            if rains[i] in filled_lakes:
                if not dry_days:
                    return []
                else:
                    day_to_dry_lake = bisect.bisect_left(dry_days, filled_lakes[rains[i]])
                    if day_to_dry_lake >= len(dry_days):
                        return []
                    ans[dry_days[day_to_dry_lake]] = rains[i]
                    dry_days.pop(day_to_dry_lake)
                    filled_lakes.pop(rains[i], None)
            if rains[i] == 0:
                dry_days.append(i)
            else:
                filled_lakes[rains[i]] = i
        return ans
