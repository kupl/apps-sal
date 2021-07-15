import numpy as np
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        
        if len(arr)==1: return min(arr[0])
        
        if len(arr[0])==2:
            return (min(arr[0][1]+arr[1][0], arr[0][0]+arr[1][1]))
        
        # arr = np.random.sample((6,6))
        
        # find the smallest 3 of the index
        sml = -np.ones((len(arr)+1, 3))
        for i in range(len(arr)):
            r = np.array(arr[i])
            sml[i+1] = (np.argsort(r)[:3])
        # print (sml)
        
        
        dp = np.zeros((len(arr)+1, 3))
        for i in range(1, len(arr)+1):
            for j in range(3):
                # print(i,j)
                col_idx = int(sml[i][j])
                sml_idx = [idx for idx in range(3) if sml[i-1][idx] != col_idx]
                # print (col_idx, sml_idx)
                # find the smallest of the last row
                # print (arr[i-1][(col_idx)])
                # print ([dp[i-1][c] for c in sml_idx])
                dp[i][j] = arr[i-1][(col_idx)] + min([dp[i-1][c] for c in sml_idx])

        print((dp[-1]))
        return int(min(dp[-1]))

