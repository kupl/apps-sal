class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        days_next = []
        n = len(rains)
        dct_lk2day = defaultdict(int)
        for (day_rev, e) in enumerate(rains[::-1]):
            if e in dct_lk2day:
                days_next.append(dct_lk2day[e])
            else:
                days_next.append(n)
            dct_lk2day[e] = n - 1 - day_rev
        days_next = days_next[::-1]
        minHp = []
        rst = []
        for (day, lk) in enumerate(rains):
            if not lk:
                if minHp:
                    d_next = heappop(minHp)
                    rst.append(rains[d_next])
                else:
                    rst.append(1)
            elif minHp and day == minHp[0]:
                return []
            else:
                if days_next[day] < n:
                    heappush(minHp, days_next[day])
                rst.append(-1)
        return rst
