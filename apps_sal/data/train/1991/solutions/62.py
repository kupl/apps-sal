class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        M = 1000000007

        @lru_cache(None)
        def f(idx, fuel):
            if fuel < 0:
                return 0
            cnt = 1 if idx == start else 0
            for (i, val) in enumerate(locations):
                if i == idx:
                    continue
                if abs(val - locations[idx]) <= fuel:
                    cnt = (cnt + f(i, fuel - abs(val - locations[idx]))) % M
            return cnt % M
        return f(finish, fuel)
