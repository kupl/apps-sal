class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = []
        freeday = []
        filled = {}

        for day, city in enumerate(rains):
            if city:
                ans.append(-1)
                if city not in filled:
                    filled[city] = day

                else:
                    if freeday and freeday[-1] > filled[city]:
                        dry_day = bisect.bisect_left(freeday, filled[city])
                        ans[freeday.pop(dry_day)] = city
                        filled[city] = day
                    else:
                        return []

            else:
                ans.append(1)
                freeday.append(day)

        return ans
