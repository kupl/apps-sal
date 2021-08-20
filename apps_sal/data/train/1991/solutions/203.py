class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def dfs(i, fuel):
            if fuel < 0:
                return 0
            elif fuel == 0:
                return 1 if i == finish else 0
            if (i, fuel) not in cache:
                cnt = 1 if i == finish else 0
                for (j, cost) in enumerate(locations):
                    if j == i:
                        continue
                    remain = fuel - abs(cost - locations[i])
                    if remain >= 0:
                        cnt += dfs(j, remain)
                cache[i, fuel] = cnt
            return cache[i, fuel]
        cache = dict()
        return dfs(start, fuel) % (10 ** 9 + 7)
