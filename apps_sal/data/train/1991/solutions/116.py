import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def chal(st, fi, x):
            if(x < 0):
                return 0
            if(st == fi):
                ans = 1
            else:
                ans = 0
            for i in range(0, len(locations)):
                if(i != st):
                    ans += chal(i, fi, x - abs(locations[i] - locations[st])) % (10**9 + 7)
            return ans % (10**9 + 7)
        return chal(start, finish, fuel)
