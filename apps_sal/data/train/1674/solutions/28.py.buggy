class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        def Util(alexTurn, index, m) -> int:
            \"\"\"
            Returns the Maximum sum of Alex
            \"\"\"
            if (index >= len(self.piles)):
                return 0
            if (index == len(self.piles) - 1):
                return self.piles[index]
            # print(f\"alexTurn = {alexTurn} index = {index} m = {m}\")
            if (self.dp[index][m] != -1):
                return self.dp[index][m]
            
            totalCounts = 0
            ans = 0

            for x in range(2*m):
                if (index + x == len(self.piles)):
                    break
                totalCounts += self.piles[index + x]
                if (index + x + 1 <= len(self.piles)):
                    nextSum = Util(not alexTurn, index + x + 1, max(m, x+1))
                    # print(index + x + 1)
                    if (index + x + 1 == len(self.piles)):
                        ans = max(ans, totalCounts)
                    else:
                        ans = max(ans, totalCounts + self.presum[index + x + 1] - nextSum)
                    # print(f\"index = {index + x + 1} m = {m} nextSum = {nextSum}\")

            self.dp[index][m] = ans
            # print(f\"index = {index} m = {m} ans = {ans} totalCounts = {totalCounts}\")

            return ans
        
        self.presum = copy.copy(piles)
        for i in reversed(range(len(piles) - 1)):
            self.presum[i] += self.presum[i + 1]
        # print(self.presum)
        self.dp = [-1]*len(piles)
        for j in range(len(piles)):
            self.dp[j] = [-1] * len(piles)
                
        self.piles = piles
        return Util(True, 0, 1)
        
