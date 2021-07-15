class Solution:
    def countRoutesUtil(self, locations , currentLocation , target , fuelLeft , dp):
        if fuelLeft < 0:
            return 0
        key = (currentLocation,fuelLeft)
        if key in dp:
            return dp[key]
        result = 0
        if currentLocation == target:
            result += 1
        for i in range(len(locations)):
            if i != currentLocation:
                result += self.countRoutesUtil(locations,i,target,fuelLeft-abs(locations[i]-locations[currentLocation]),dp)
                result %= (10 ** 9 + 7)
        dp[key] = result % (10 ** 9 + 7)
        return dp[key]
        
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        return self.countRoutesUtil(locations,start,finish,fuel,{})

