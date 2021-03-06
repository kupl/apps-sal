class Solution:

    def helper(self, cur_loc, fuel):
        if fuel < 0:
            return 0
        if (cur_loc, fuel) in self.mem:
            return self.mem[cur_loc, fuel]
        ans = 0
        if cur_loc == self.finish:
            ans += 1
        for nxt in range(len(self.locations)):
            if nxt != cur_loc:
                ans += self.helper(nxt, fuel - abs(self.locations[cur_loc] - self.locations[nxt]))
        ans = ans % (10 ** 9 + 7)
        self.mem[cur_loc, fuel] = ans
        return ans

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.finish = finish
        self.locations = locations
        self.mem = {}
        ans = self.helper(start, fuel)
        return ans


class Solution1:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def cost(i, j):
            return abs(locations[i] - locations[j])

        @lru_cache(None)
        def dfs(cur, remain_fuel):
            if remain_fuel < 0:
                return 0
            return sum((dfs(next_city, remain_fuel - cost(cur, next_city)) for next_city in range(len(locations)) if cur != next_city)) + (cur == finish)
        constant = 10 ** 9 + 7
        return dfs(cur=start, remain_fuel=fuel) % constant
