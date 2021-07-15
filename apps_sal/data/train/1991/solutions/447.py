class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        def cnt(locations, cur, fuel, memo):
            if (cur, fuel) in memo:
                return memo[cur, fuel]
            
            n = len(locations)
            result = 0
            if cur == finish:
                result = 1
                
            for i in range(n):
                if i != cur:
                    cost = abs(locations[i] - locations[cur])
                    if cost <= fuel:
                        result += cnt(locations, i, fuel-cost, memo)
                    
            memo[cur, fuel] = result
            return result

        
        def dp(locations, start, finish, fuel):
            n = len(locations)
            tbl = [[0 for j in range(fuel+1)] for i in range(n)]
            tbl[start][0] = 1   # itself to itself. always a way

            for f in range(1, fuel+1):
                # start node -> start node at least one way. (without via other nodes). 0 fuel need
                tbl[start][f] = 1 
                
                # start node -> move via other nodes -> cur node
                for cur in range(n):
                    for last in range(n):
                        if cur != last:
                            cost = abs(locations[cur] - locations[last])
                            if f >= cost:
                                tbl[cur][f] += tbl[last][f-cost]

            return tbl[finish][fuel]
        
        # return cnt(locations, start, fuel, {}) % (10**9+7)
        return dp(locations, start, finish, fuel) % (10**9+7)
