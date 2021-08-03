import bisect


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry_days = []
        last_rainy_day = {}
        ans = [-1 if rain > 0 else 1 for rain in rains]
        for i, rain in enumerate(rains):
            if not rain:
                dry_days.append(i)
            else:
                if rain not in last_rainy_day:
                    last_rainy_day[rain] = i
                else:
                    if not dry_days:
                        return []
                    else:
                        index = bisect.bisect_left(dry_days, last_rainy_day[rain])
                        if index >= len(dry_days):
                            return []
                        ans[dry_days.pop(index)] = rain
                        last_rainy_day[rain] = i
        return ans
