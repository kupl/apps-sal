class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        '''
        dp = [[0]*201 for _ in range(101)]
        dp[start][fuel] = 1  # start pos
        res = 0
        locs = locations
        for f in range(fuel-1,-1,-1):
          for i in range(len(locs)):   
            for j in range(len(locs)):
              if i!=j :
                d = abs(locs[i]-locs[j])
                if f+d>200: continue

                dp[i][f] = (dp[i][f] + dp[j][f+d])%1000000007

        # for rw in dp[:len(locs)]:
        #   print (rw[:fuel+1])
        res = sum([v%1000000007 for v in dp[finish]])%1000000007
        '''

        locs = locations
        dp = [[0] * (fuel + 1) for _ in range(len(locs))]
        dp[start] = [1] * (fuel + 1)  # start pos
        res = 0

        for f in range(1, fuel + 1):
            for i in range(len(locs)):
                for j in range(len(locs)):
                    if i != j:
                        d = abs(locs[i] - locs[j])
                        if f - d >= 0:
                            dp[i][f] = (dp[i][f] + dp[j][f - d]) % 1000000007

        # for rw in dp[:len(locs)]:
        #   print (rw[:fuel+1])
        res = dp[finish][fuel] % 1000000007

        return res
