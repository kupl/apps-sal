from typing import List
from collections import deque


class Solution:

    # Brute Force
    #     def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
    #         ans = 0

    #         q = deque([(start, fuel)])

    #         while q:
    #             curr, tel = q.popleft()
    #             if curr == finish:
    #                 ans+=1%(10**9 + 7   )

    #             for i in range(len(locations)):
    #                 if i!=curr and tel-abs(locations[i]-locations[curr])>=0:
    #                     q.append((i, tel-abs(locations[i]-locations[curr])))
    #         return ans

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def aux(curr, tel):
            if tel < 0:
                return 0
            if (curr, tel) in dp:
                return dp[(curr, tel)]
            ans = 1 if curr == finish else 0

            for i in range(len(locations)):
                if i != curr:
                    ans += aux(i, tel - abs(locations[i] - locations[curr])) % M
            dp[(curr, tel)] = ans % M
            return ans % M
        M = 10**9 + 7
        dp = dict()
        return aux(start, fuel) % M
