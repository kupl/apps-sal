class Solution:

    def minFallingPathSum(self, cost: List[List[int]]) -> int:
        numHouses = len(cost)
        numMaterials = len(cost[0])
        dp = cost[0]
        for h in range(1, numHouses):
            newRow = []
            for m in range(1, numMaterials + 1):
                prevCost = min([dp[prevMat - 1] for prevMat in range(1, numMaterials + 1) if prevMat != m])
                newRow.append(cost[h][m - 1] + prevCost)
            dp = newRow
        return min(dp)
