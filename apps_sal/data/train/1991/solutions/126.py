class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if abs(locations[start] - locations[finish]) > fuel:
            return 0
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(node, fu):
            an = 0
            if node == finish:
                an += 1
            for i in range(len(locations)):
                if i != node and abs(locations[node] - locations[i]) <= fu:
                    an += dfs(i, fu - abs(locations[node] - locations[i]))
            return an
        return dfs(start, fuel) % mod
