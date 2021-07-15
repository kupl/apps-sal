class Solution:
    MODULO = 10**9+7
    
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        my_dp = dict()
        return Solution.get_dp(my_dp, locations, start, finish, fuel)
    
    
    @staticmethod
    def get_dp(dp, locations, start, finish, fuel):
        if (start, finish, fuel) not in dp:
            total_ways = 0
            
            if start == finish:
                total_ways = 1
            
            for idx, pos in enumerate(locations):
                if idx != start and abs(locations[start]-locations[idx]) <= fuel:
                    total_ways = (total_ways + Solution.get_dp(dp, locations, idx, finish,
                                                               fuel - abs(locations[start]-locations[idx]))) % Solution.MODULO
            dp[(start, finish, fuel)] = total_ways
                
        
        return dp[(start, finish, fuel)]
