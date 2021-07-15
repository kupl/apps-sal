class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        def getLocations(location, fuel):
            if (location, fuel) in mem:
                return mem[(location, fuel)]
            if fuel < 0:
                return 0
            ans = 0
            if location == locations[finish]:
                ans = 1
            
            for newLoc in locations:
                if newLoc != location:
                    ans += getLocations(newLoc, fuel - abs(location - newLoc))
            mem[(location, fuel)] = ans
            
            return ans
        mem = {}
        return getLocations(locations[start], fuel) % (10**9 +7)

