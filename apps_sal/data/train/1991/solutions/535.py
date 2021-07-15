class Solution:
    # https://discord.com/channels/612060087900438538/612587060099940372/751834983198359674

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(i, f):
            # Number of routes to finish from city u, with f fuel
            ans = i == finish
            for j in range(len(locations)):
                if j != i:
                    delta = abs(locations[i] - locations[j])
                    if delta <= f:
                        ans += dfs(j, f - delta)
            return ans
        
        return dfs(start, fuel) % (10**9 + 7)
