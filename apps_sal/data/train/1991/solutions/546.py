class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)
        DP = [[-1]*(fuel+1) for i in range(n)]
        DP[finish][0]=1
        pos_finish = locations[finish]
        def search(loc, fuel):
            if DP[loc][fuel]!=-1:
                return DP[loc][fuel]
            DP[loc][fuel]=0
            pos = locations[loc]
            toEnd = abs(pos-pos_finish)
            if toEnd > fuel:
                return 0
            #elif toEnd == fuel:
            #    DP[loc][fuel]=1
            #    return 1
            # toEnd >= fuel
            for loc2 in range(n):
                if loc2 == loc:
                    continue
                tmp = abs(pos-locations[loc2])
                if tmp<=fuel:
                    DP[loc][fuel]+=search(loc2, fuel-tmp)
            DP[loc][fuel] += loc == finish
            DP[loc][fuel] %= MOD
            return DP[loc][fuel]
        search(start, fuel)
        return search(start, fuel)
