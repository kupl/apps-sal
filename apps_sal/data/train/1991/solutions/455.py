class Solution:
    def countRoutes(self, l: List[int], start: int, final: int, fuel: int) -> int:

        if abs(l[start] - l[final]) > fuel:
            return 0
        mod = 10**9 + 7
        n = len(l)
        # dp[i][k] = i fuel left and at  l[k]
        dp = [[0] * n for i in range(fuel + 1)]
        s, f = l[start], l[final]

        l.sort()
        start, final = bisect.bisect_left(l, s), bisect.bisect_left(l, f)
        print(s, f, start, final, l)
        dp[fuel][start] = 1
        # print(dp)
        for f in range(fuel, -1, -1):
            for p in range(n):
                for np in range(n):
                    if np == p or abs(l[np] - l[p]) > f:
                        continue
                    diff = abs(l[np] - l[p])
                    dp[f - diff][np] += dp[f][p]
            # print(dp)
        res = sum([dp[z][final] for z in range(fuel + 1)])
        return res % (mod)
