class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(maxsize=None)
        def traverse(curr: int, fuel: int) -> int:
            if fuel < 0:
                return 0
            res = 0
            if curr == finish:
                res += 1
                if fuel == 0:
                    return res
            for i, location in enumerate(locations):
                if i != curr:
                    res += traverse(i, fuel - abs(location - locations[curr]))
            return res
        return traverse(start, fuel) % (10**9 + 7)
