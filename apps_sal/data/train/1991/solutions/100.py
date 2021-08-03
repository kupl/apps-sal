class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(locations)

        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(locations[i] - locations[j])
                graph[i].append((j, cost))
                graph[j].append((i, cost))

        @lru_cache(None)
        def dfs(i, budget):
            if budget < 0:
                return 0

            res = 1 if i == finish else 0
            if budget == 0:
                return res

            for nei, cost in graph[i]:
                res += dfs(nei, budget - cost)
                res %= MOD

            return res

        res = dfs(start, fuel)

        return res % MOD
