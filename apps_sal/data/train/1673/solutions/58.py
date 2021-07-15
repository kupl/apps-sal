import heapq
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
       
        l = len(arr)
        dp = [[0 for i in range(l)] for j in range(l)]
        res = inf
    
        for j in range(l):
            dp[0][j] = arr[0][j]
        
        print(dp)
        
        for i in range(1,l):
            for j in range(len(dp)):
                minr = min([dp[i-1][k] for k in range(l) if k != j])
                dp[i][j] = arr[i][j] + minr
                if i == l - 1:
                    res = min(res, dp[i][j])
        
        return res
                          
        
                           
                         
        
       
        
        
 # [1,2,3]
 # [4,5,6]
 # [7,8,9]

[[-2,-18,31,-10,-71,82,47,56,-14,42],
 [-95,3,65,-7,64,75,-51,97,-66,-28],
 [36,3,-62,38,15,51,-58,-90,-23,-63],
 [58,-26,-42,-66,21,99,-94,-95,-90,89],
 [83,-66,-42,-45,43,85,51,-86,65,-39],
 [56,9,9,95,-56,-77,-2,20,78,17],
 [78,-13,-55,55,-7,43,-98,-89,38,90],
 [32,44,-47,81,-1,-55,-5,16,-81,17],
 [-87,82,2,86,-88,-58,-91,-79,44,-9],
 [-96,-14,-52,-8,12,38,84,77,-51,52]]


