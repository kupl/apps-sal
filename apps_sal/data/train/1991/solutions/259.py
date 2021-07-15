class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        memo = {}
        mod = 10**9+7
        def dp(f,c):
            if f == 0 and c == finish:
                return 1
            else:
                if (f,c) not in memo:
                    if c == finish and f > 0:
                        ans = 1
                    else:
                        ans = 0
                    for nxt in range(len(locations)):
                        if nxt == c:continue
                        dis = abs(locations[c]-locations[nxt])
                        if dis <= f:
                            ans += dp(f-dis,nxt)
                    memo[f,c] = ans%mod
                return memo[f,c]
        return dp(fuel,start)
