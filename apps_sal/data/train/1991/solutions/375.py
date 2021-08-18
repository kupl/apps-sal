class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start = locations[start]
        finish = locations[finish]
        locations.sort()
        res = 0
        dict = {}

        def dfs(start, finish, fuel):
            if (start, fuel) in dict:
                return dict[(start, fuel)]
            route = 0
            for index, val in enumerate(locations):

                if val != start and abs(val - start) <= fuel:
                    if val == finish:
                        route += 1
                    dict[(val, fuel - abs(val - start))] = dfs(val, finish, fuel - abs(val - start))
                    route += dict[(val, fuel - abs(val - start))]
            return route

        res = dfs(start, finish, fuel)
        if start == finish:
            res += 1
        return res % (10**9 + 7)
