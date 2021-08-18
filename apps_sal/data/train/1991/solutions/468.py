class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        n = len(locations)
        MOD = 10**9 + 7

        nxtFuel = defaultdict(list)
        for node in range(n):
            for nxt in range(n):
                if node == nxt:
                    continue
                use = abs(locations[node] - locations[nxt])
                nxtFuel[node].append((nxt, use))

        @lru_cache(None)
        def dp(used, node):
            if used > fuel:
                return 0
            res = 1 if node == finish else 0

            for nxt, use in nxtFuel[node]:
                res += dp(used + use, nxt) % MOD
            return res

        return dp(0, start) % MOD
