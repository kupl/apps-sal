class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        R,C = len(arr), len(arr[0])
        
        DP = [[float(\"inf\")]*C for i in range(R)]
        
        #fill the 1st row with same values:
        for j in range(C):
            DP[0][j]=arr[0][j]
        
        for i in range(1,R):
            for j in range(C):
                #if left edge--> then nothing on left
                if(j==0):
                    DP[i][j] = min(arr[i][j]+DP[i-1][k] for k in range(j+1,C))
                
                #if right edge--> then nothing on right
                elif(j==C-1):
                    DP[i][j] = min(arr[i][j]+DP[i-1][k] for k in range(j-1,-1,-1))
                    
                #else--> both from left & right
                else:
                    left = min(DP[i-1][k] for k in range(0,j))
                    right = min(DP[i-1][k] for k in range(j+1,C))
                    DP[i][j] = min(left+arr[i][j],right+arr[i][j])
        
        return min(DP[R-1])
        
        
