class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 1000000007

        @lru_cache(None)
        def go(pos, fuel):
            # print(pos)
            temp = 0
            if fuel < 0:
                return 0
            ans = 0
            if pos == finish:
                ans += 1
            for i in range(n):
                if i == pos:
                    continue
                ans += (go(i, fuel - abs(locations[pos] - locations[i])))
            return ans % MOD
        return go(start, fuel)
