
class Solution(object):
    def minFallingPathSum(self, a):
        \"\"\"
        :type arr: List[List[int]]
        :rtype: int
        \"\"\"
        n=len(a)
        if(n==1):
            return a[0][0]
        dp=[[0 for i in range(n)]for j in range(n)]
        pos1=-1
        pos2=-1
        for i in range(n):
            print(pos1,pos2)
            for j in range(n):
                dp[i][j]=a[i][j]
                if i==0:
                    continue
                if j==pos1:
                    dp[i][j]+=dp[i-1][pos2]
                else:
                    dp[i][j]+=dp[i-1][pos1]
            pos1=0
            pos2=1
            if dp[i][0]>dp[i][1]:
                pos1,pos2=pos2,pos1
            for j in range(2,n):
                if dp[i][j]<dp[i][pos1]:
                    pos2=pos1
                    pos1=j
                elif dp[i][j]<dp[i][pos2]:
                    pos2=j
        print(dp)      
        return dp[-1][pos1]
