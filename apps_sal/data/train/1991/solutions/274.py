class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        return self.helper(locations, start, finish, fuel, {})
    
    def helper(self, locations, start, finish, fuel, memo):
        if fuel < 0:
            return 0
        
        if (start, fuel) in memo:
            return memo[(start, fuel)]
        
        result = 0
        if start == finish:
            result = 1
              
        for i in range(len(locations)):
            if i != start:
                result = (result + self.helper(locations, i, finish, fuel - abs(locations[i] - locations[start]), memo)) % 1000000007                
        memo[(start, fuel)] = result
        return result
