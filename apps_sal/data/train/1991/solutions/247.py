class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.res = 0
        memo = {}
        def dfs(cur_city, fuel):
            if (cur_city, fuel) in memo: return memo[cur_city, fuel]
            if fuel < 0:
                return 0
            cnt = 1 if cur_city == finish else 0 #now at finish, fuel cost is 0
            for i in range(len(locations)):
                if i == cur_city: continue
                cnt += dfs(i, fuel - abs(locations[i] - locations[cur_city])) #add other possible ways.
            memo[cur_city, fuel] = cnt
            return cnt
            
        return dfs(start, fuel)%(10**9 + 7)

