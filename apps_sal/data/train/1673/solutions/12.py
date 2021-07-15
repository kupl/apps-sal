class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[-100 for _ in range(len(arr[0]))] for _ in range(len(arr))]
        mi, mis = 100, 100
        index = -1
        for j in range(len(arr[0])):
            dp[0][j] = arr[0][j]
            if dp[0][j] <= mi:
                mis = mi
                mi = dp[0][j]
                index = j
            elif dp[0][j] < mis:
                mia = dp[0][j]
        candidate = [mi, mis, index]
        #print(candidate)
        
        for i in range(1, len(arr)):
            nxt = [float(\"inf\"), float(\"inf\"), -1]
            for j in range(len(arr[0])):
                if j != candidate[2]:
                    dp[i][j] = candidate[0] + arr[i][j]
                    
                else:
                    dp[i][j] = candidate[1] + arr[i][j]
                
                if dp[i][j] <= nxt[0]:
                    nxt[1] = nxt[0]
                    nxt[0] = dp[i][j]
                    nxt[2] = j
                elif dp[i][j] < nxt[1]:
                    nxt[1] = dp[i][j]
            candidate = nxt[:]
            #print(candidate)
        return min(dp[-1])
