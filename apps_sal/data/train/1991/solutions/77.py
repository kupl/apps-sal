class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(i: int, f: int) -> int:
            return 0 if f < 0 else (1 if i == finish else 0) + sum(0 if i == j else dfs(j, f - abs(locations[j] - locations[i])) for j in range(len(locations)))
        return dfs(start, fuel) % 1000000007
        # dp = [[-1 for _ in range(fuel+1)] for _ in locations]
        # def search(start, fuel):
        #     if fuel == 0:
        #         if start == finish:
        #             return 1
        #         return 0
        #     if dp[start][fuel] != -1:
        #         return dp[start][fuel]
        #     dp[start][fuel] = 1 if start == finish else 0
        #     for i in range(len(locations)):
        #         left = fuel - abs(locations[i] - locations[start])
        #         if i != start and left >= 0:
        #             dp[start][fuel] += search(i, left) 
        #     return dp[start][fuel] % 1000000007
        # return search(start, fuel) % 1000000007

