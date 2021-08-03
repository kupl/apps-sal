class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # loop  day , lk ,   if 0 ,  clean the immediate next overflow,  if not 0 , overflow or fill empty  depends on if in next schedule
        # https://leetcode.com/problems/avoid-flood-in-the-city/discuss/698328/python-faster-than-10000-of-python-online-submissions-for-avoid-flood-in-the-city
        # https://leetcode.jp/leetcode-avoid-flood-in-the-city-%e8%a7%a3%e9%a2%98%e6%80%9d%e8%b7%af%e5%88%86%e6%9e%90/

        days_next = []
        n = len(rains)
        dct_lk2day = defaultdict(int)  # lake:day ,  last time happened day
        for day_rev, e in enumerate(rains[::-1]):
            if e in dct_lk2day:
                days_next.append(dct_lk2day[e])  # existing day
            else:
                days_next.append(n)     # last day + 1  , next will be outside
            dct_lk2day[e] = n - 1 - day_rev  # update current day
        days_next = days_next[::-1]     # reverse

        # loop again,  put next day to minheap, 0 , clean, non0 fill or overflow
        minHp = []
        rst = []
        for day, lk in enumerate(rains):
            if not lk:  # 0
                if minHp:
                    d_next = heappop(minHp)  # 1st ele
                    rst.append(rains[d_next])  # that lake
                else:
                    rst.append(1)  # 1st lake
            else:
                if minHp and day == minHp[0]:  # not cleaned up , overflow  , eval and left first
                    return []
                else:       # cleaned , will fill
                    if days_next[day] < n:    # if needs to be cleaned in future
                        heappush(minHp, days_next[day])  # next coming time
                    rst.append(-1)

        return rst
