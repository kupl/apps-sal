class Solution:
    def countRoutes(self, locacs: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1]*(fuel+1) for _ in range(len(locacs))]
        def go(at, f):
            if f <= 0:
                return 1 if at == finish else 0
            if dp[at][f] >= 0:
                return dp[at][f]
            ans = 1 if at == finish else 0
            for to, loc in enumerate(locacs):
                if to == at:
                    continue
                c = abs(locacs[at]-loc)
                ans += go(to, f-c) if f >= c else 0
            dp[at][f] = ans
            return ans
        return go(start, fuel) % (10**9+7)


