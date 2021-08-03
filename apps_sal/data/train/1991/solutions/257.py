class Solution:
    def dfs(self, locations, memo, current, finish, remain_fuel):
        if remain_fuel < 0:
            return 0
        if remain_fuel == 0:
            return 1 if current == finish else 0
        if (current, remain_fuel) in memo:
            return memo[(current, remain_fuel)]
        l = len(locations)
        ans = 0 if current != finish else 1
        for i in range(l):
            if i == current:
                continue
            dist = abs(locations[current] - locations[i])
            ans += self.dfs(locations, memo, i, finish, remain_fuel - dist)
        memo[(current, remain_fuel)] = ans
        return ans

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        NUM = 10**9 + 7
        memo = dict()
        return self.dfs(locations, memo, start, finish, fuel) % NUM
