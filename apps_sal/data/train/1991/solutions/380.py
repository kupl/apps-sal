class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        res, mod, cache = 0, 10 ** 9 + 7, {}
        # cache[(i, fuel)]: how many ways to start from city i with initial fuel to go to city end

        def dfs(s, fuel):
            if fuel <= 0:
                return 0
            if (s, fuel) not in cache:
                cache[(s, fuel)] = 0
                for city in range(len(locations)):
                    if city != s:
                        cache[(s, fuel)] += dfs(city, fuel - abs(locations[city] - locations[s])) % mod
                        if city == finish and fuel - abs(locations[city] - locations[s]) >= 0:
                            cache[(s, fuel)] += 1
            return cache[(s, fuel)] % mod
        return dfs(start, fuel) + (0 if start != finish else 1)


'''
[2,1,5]
0
0
3
[2,3,6,8,4]
1
3
5
 [4,3,1]
 1
 0
 6
 [5,2,1]
 0
 2
 3
 [1,2,3]
 0
 2
 40
'''
