class Solution:
    
    
    def minFallingPathSum(self, cost: List[List[int]]) -> int:
        
        numHouses = len(cost)
        cols = len(cost[0])
        dp = cost[0]

        for h in range(1, numHouses):
            newRow = [0 for _ in range(cols)]
            for m in range(1, cols+1):
                prevCost = min([dp[prevMat-1]
                    for prevMat in range(1, cols+1)
                    if prevMat != m])
                newRow[m-1] = (cost[h][m-1] + prevCost)
            dp = newRow

        return min(dp)
