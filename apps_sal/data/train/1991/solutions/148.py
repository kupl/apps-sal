class Solution:
    def helper(self, locations, index, finish, fuelLeft, cache):
        if (index, fuelLeft) in cache:
            return cache[(index, fuelLeft)]
        
        result = 0
        if index == finish and fuelLeft >= 0:
            result += 1
        
        for i in range(len(locations)):
            if i == index:
                continue
            
            fuelUsed = abs(locations[index] - locations[i])
            if fuelLeft >= fuelUsed:
                result += self.helper(locations, i, finish, fuelLeft - fuelUsed, cache)
        
        cache[(index, fuelLeft)] = result
        return result
    
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        result = self.helper(locations, start, finish, fuel, {})
        return result % (10**9+7)

