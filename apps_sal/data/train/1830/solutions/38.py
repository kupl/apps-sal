class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = []
        zero = []
        full = {}
        for (day, city) in enumerate(rains):
            if city:
                ans.append(-1)
                if city in full:
                    if zero and zero[-1] > full[city]:
                        dry = bisect.bisect_left(zero, full[city])
                        ans[zero.pop(dry)] = city
                        full[city] = day
                    else:
                        return []
                else:
                    full[city] = day
            else:
                ans.append(1)
                zero.append(day)
        return ans
