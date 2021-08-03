class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def rec(current, f):
            if f < 0:
                return 0
            else:
                return (1 if current == finish else 0) + sum(0 if i == current else rec(i, f - abs(locations[current] - locations[i])) for i in range(len(locations)))

        return rec(start, fuel) % 1000000007
