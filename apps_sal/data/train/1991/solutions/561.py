class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 1_000_000_007

        from functools import lru_cache

        @lru_cache(None)
        def backtrack(index, remaining_gas):
            if index == finish and remaining_gas == 0:
                return 1
            if remaining_gas == 0 and index != finish:
                return 0

            count = 0
            if index == finish:
                count = 1
            for i in range(len(locations)):
                if i == index:
                    continue
                dist = abs(locations[i] - locations[index])
                if dist <= remaining_gas:
                    count = (count + backtrack(i, remaining_gas - dist)) % MOD
            return count

        return backtrack(start, fuel)
