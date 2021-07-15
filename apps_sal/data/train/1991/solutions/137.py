class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        cache = {}

        def dp(i, fuel):
            if (i, fuel) in cache:
                return cache[(i, fuel)]

            count = 1 if i == finish else 0

            for j in range(len(locations)):
                if i != j:
                    dist = abs(locations[i] - locations[j])
                    if dist <= fuel:
                        count += dp(j, fuel - dist)

            cache[(i, fuel)] = count
            return count

        return dp(start, fuel) % (10**9 + 7)
