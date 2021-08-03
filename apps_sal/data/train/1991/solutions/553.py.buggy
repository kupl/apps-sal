class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        \"\"\"
        FAACK.. 
        Was able to solve in biweekly contest (sat morning 10:30 EST contest - sep 5 2020)
        I don't know... I was able to solve a hard DP question and not able to solve 2 medium questions...
        
        \"\"\"
        @lru_cache(maxsize = None)
        def helper(cur_city, cur_fuel):
            if cur_fuel < 0: return 0
            else:
                s = int(cur_city == finish)
                for i in range(len(locations)):
                    rem_fuel = cur_fuel - abs(locations[cur_city] - locations[i])
                    if i != cur_city and rem_fuel >= 0: s += helper(i, rem_fuel)
            return s
        return helper(start, fuel) % (10 ** 9 + 7)
    
        \"\"\"
        TLE
        
        First saw in biweekly contest (sat morning 10:30 EST contest - sep 5 2020)
        \"\"\"
        # def helper(cur_city, cur_fuel):
        #     if cur_fuel >= 0:
        #         if cur_city == finish: self.res = self.res + 1
        #         for i in range(len(locations)):
        #             rem_fuel = cur_fuel - abs(locations[cur_city] - locations[i])
        #             if i != cur_city and rem_fuel >= 0: helper(i, rem_fuel)
        # self.res = 0
        # helper(start, fuel)
        # return self.res
