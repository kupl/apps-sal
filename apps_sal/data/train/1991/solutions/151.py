class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        md=10**9+7
        # dp[i][j]...vertex i,fuel j
        n=len(locations)
        dp=[[0]*(fuel+1) for _ in range(n)]
        dp[start][0]=1
        for j in range(fuel):
            for i in range(n):
                pre=dp[i][j]%md
                if pre==0:continue
                for ni in range(n):
                    if i==ni:continue
                    nj=j+abs(locations[i]-locations[ni])
                    if nj>fuel:continue
                    dp[ni][nj]+=pre
        ans=sum(dp[finish])%md
        return ans

