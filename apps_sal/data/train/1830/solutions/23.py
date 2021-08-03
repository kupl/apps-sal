class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n

        last = {}

        dry_days = []

        for idx, r in enumerate(rains):
            if r == 0:
                dry_days.append(idx)
            else:
                if r in last:
                    found = False
                    j = 0
                    while j < len(dry_days):
                        if dry_days[j] > last[r]:
                            ans[dry_days[j]] = r
                            found = True
                            break
                        j += 1

                    if not found:
                        return []
                    dry_days.pop(j)
                last[r] = idx

        while dry_days:
            dry_day = dry_days.pop()
            ans[dry_day] = 1

        return ans
