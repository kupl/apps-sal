class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        (res, mod, cache) = (0, 10 ** 9 + 7, {})

        def dfs(s, fuel):
            if fuel <= 0:
                return 0
            if (s, fuel) not in cache:
                cache[s, fuel] = 0
                for city in range(len(locations)):
                    if city != s:
                        cache[s, fuel] += dfs(city, fuel - abs(locations[city] - locations[s])) % mod
                        if city == finish and fuel - abs(locations[city] - locations[s]) >= 0:
                            cache[s, fuel] += 1
            return cache[s, fuel] % mod
        return dfs(start, fuel) + (0 if start != finish else 1)


'\n[2,1,5]\n0\n0\n3\n[2,3,6,8,4]\n1\n3\n5\n [4,3,1]\n 1\n 0\n 6\n [5,2,1]\n 0\n 2\n 3\n [1,2,3]\n 0\n 2\n 40\n'
