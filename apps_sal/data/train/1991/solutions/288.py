class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        m = collections.defaultdict(lambda: 0)
        n = len(locations)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    m[(i, j)] = abs(locations[i] - locations[j])
        memo = {}
        MOD = 10 ** 9 + 7

        def dfs(cur, target, fuel):
            nonlocal n
            if fuel < 0:
                return 0
            elif (cur, fuel) in memo:
                return memo[(cur, fuel)]
            else:
                cnt = 1 if cur == target else 0
                for i in range(n):
                    if i != cur:
                        cnt += dfs(i, target, fuel - m[(i, cur)])
                memo[(cur, fuel)] = cnt
                return memo[(cur, fuel)]

        return dfs(start, finish, fuel) % MOD
