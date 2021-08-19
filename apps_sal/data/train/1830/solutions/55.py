from bisect import bisect_left


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        last_appear = {}
        dry_days = []
        for (idx, lake) in enumerate(rains):
            if lake == 0:
                dry_days.append(idx)
                continue
            if lake in last_appear:
                first_0 = bisect_left(dry_days, last_appear[lake])
                if first_0 == len(dry_days):
                    return []
                ans[dry_days[first_0]] = lake
                dry_days.pop(first_0)
                last_appear.pop(lake)
            last_appear[lake] = idx
        for day in dry_days:
            ans[day] = 1
        return ans
