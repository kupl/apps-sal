class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mem = {}
        mod = 10**9 + 7

        def helper(ind, f):
            cnt = 0
            if (ind, f) in mem:
                return mem[(ind, f)]
            if ind < 0 or ind > n - 1:
                return 0
            if ind == finish and f >= 0:
                cnt += 1
            for i in range(n):
                if i != ind and f - abs(locations[ind] - locations[i]) >= 0:
                    cnt += helper(i, f - abs(locations[ind] - locations[i])) % mod
            mem[(ind, f)] = cnt
            return cnt % mod

        return helper(start, fuel) % mod
