class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @functools.lru_cache(None)
        def dp(i, fuel):
            count = 1 if i == finish else 0

            for j in range(len(locations)):
                if i != j:
                    dist = abs(locations[i] - locations[j])
                    if dist <= fuel:
                        count += dp(j, fuel - dist)

            return count

        return dp(start, fuel) % (10**9 + 7)
