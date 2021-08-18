class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def cost(i, j): return abs(locations[i] - locations[j])

        @lru_cache(None)
        def dfs(cur, remain_fuel):

            if remain_fuel < 0:
                return 0

            return sum(dfs(j, remain_fuel - cost(cur, j))for j in range(len(locations)) if cur != j) + (cur == finish)

        return dfs(cur=start, remain_fuel=fuel) % (10 ** 9 + 7)
