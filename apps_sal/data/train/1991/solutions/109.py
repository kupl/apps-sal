class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        mod = (10**9)+7
        
        @lru_cache(None)
        def rec(cur, rem):
            if rem < 0:
                return 0
            ans = (cur == finish)
            for i in range(N):
                if i == cur:
                    continue
                nxt_rem = rem - abs(locations[cur] - locations[i])
                ans += rec(i, nxt_rem)
                if ans >= mod:
                    ans -= mod
            return ans
        
        return rec(start, fuel)
