class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        mod = (10**9) + 7

        @lru_cache(None)
        def rec(cur, rem):
            if rem <= 0:
                return cur == finish and rem == 0
            ans = (cur == finish)
            for i in range(N):
                if i == cur:
                    continue
                ans += rec(i, rem - abs(locations[cur] - locations[i]))

            return ans % mod

        return rec(start, fuel)
