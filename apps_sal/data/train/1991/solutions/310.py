class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}
        n = len(locations)
        mod = 10**9 + 7
        def rec(start,end,fuel,n):
            res = 0
            if fuel < 0:
                return res
            if (start,end,fuel) in dp:
                return dp[(start,end,fuel)]
            if start == end:
                res += 1
            for i in range(n):
                if i == start:
                    continue
                res += rec(i,end,fuel-abs(locations[i]-locations[start]),n)
            dp[(start,end,fuel)] = res
            return res
        return rec(start,finish,fuel,n) % mod
