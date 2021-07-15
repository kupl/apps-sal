class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start = locations[start]
        finish = locations[finish]
        locations.sort()
        #print(locations)
        res = 0
        dict = {}
        def dfs(start, finish, fuel):
            #[2,3,4,6,8] 3->6
            #print((start, finish, fuel))
            if (start, fuel) in dict:
                return dict[(start, fuel)]
            route = 0
            for val in locations:
                if val != start and abs(val - start) <= fuel:
                    if val == finish:
                        route += 1
                    
                    dict[(val, fuel-abs(val - start))] = dfs(val, finish, fuel-abs(val - start))
                    route += dict[(val, fuel-abs(val - start))]
            return route
                    
        res = dfs(start, finish, fuel)
        if start == finish:
            res += 1
        return res%(10**9+7)
