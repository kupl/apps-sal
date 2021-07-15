from functools import lru_cache

class Solution:
    locations = list()
    @lru_cache(None)
    def helper(self, start, finish, fuel):
        if(fuel < abs(self.locations[start]-self.locations[finish])):
            return 0
        res = 0
        for i,v in enumerate(self.locations):
            if(i != start):
                res += self.helper(i, finish, fuel-abs(v-self.locations[start]))
        if(start == finish):
            res += 1
        return res  
    def countRoutes(self, l, start, finish, fuel):
        self.locations = l
        return self.helper(start,finish,fuel) % 1000000007;
