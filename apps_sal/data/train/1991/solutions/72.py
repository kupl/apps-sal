from functools import lru_cache

class Solution:
    M = 10**9 + 7
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(maxsize=None)
        def R(dest, f):
            if f > 0:
                return (sum(R(i, f - abs(locations[i] - locations[dest]))
                            for i in range(len(locations)) if i != dest)
                        + int(dest == start)
                       ) % self.M
            return int(f == 0 and dest == start)
        
        return R(finish, fuel)
