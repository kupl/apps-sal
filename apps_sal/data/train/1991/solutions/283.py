class Solution:
    def countRoutesHelper(self, locations, currentLocation, finish, fuel):
        if fuel < 0:
            return 0
        else:
            if (currentLocation, fuel) in self.dp:
                return self.dp[(currentLocation, fuel)]
            else:
                res = 0
                if currentLocation == finish:
                    res += 1
                for i in range(len(locations)):
                    if i != currentLocation:
                        res += self.countRoutesHelper(locations, i, finish, fuel - abs(locations[currentLocation] - locations[i]))
                self.dp[(currentLocation, fuel)] = res
                return res
        
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.dp = {}
        return self.countRoutesHelper(locations, start, finish, fuel) % (10**9 + 7)
