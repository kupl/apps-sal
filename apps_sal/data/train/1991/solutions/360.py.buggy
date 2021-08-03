class Solution(object):
    
    def helper(self, city, fuel_left):

        if (city, fuel_left) not in self.dp:
            ans = 0

            if fuel_left >= 0:

                if city == self.finish:
                    ans = 1

                for index in range(self.n):
                    if index != city:
                        fuel_needed = abs(self.locations[index] - self.locations[city])
                        ans += self.helper(index, fuel_left - fuel_needed)

            self.dp[(city, fuel_left)] = ans

        return self.dp[(city, fuel_left)]
    
    def countRoutes(self, locations, start, finish, fuel):
        \"\"\"
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        \"\"\"
        
        self.n = len(locations)
        self.locations = locations
        self.finish = finish
        
        self.dp = {}
        
        mod = (10**9) + 7
        return self.helper(start, fuel) % mod
                
            
