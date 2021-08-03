class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        def Util(alexTurn, index, m) -> int:
            \"\"\"
            Returns the Maximum sum of Alex
            \"\"\"
            if (index >= len(self.piles)):
                return 0
            turn = 1 if alexTurn is True else 0

            # print(f\"alexTurn = {alexTurn} index = {index} m = {m}\")
            if (self.dp[turn][index][m] != -1):
                return self.dp[turn][index][m]
            
            totalCounts = 0
            ans = 0
            if (alexTurn):
                ans = 0
                for x in range(2*m):
                    if (index + x == len(self.piles)):
                        break
                    totalCounts += self.piles[index + x]
                    alexSum = Util(not alexTurn, index + x + 1, max(m, x+1))
                    # print(f\"alexSum = {alexSum} index = {index} x = {x} M = {max(m, x + 1)} ans = {alexSum + totalCounts}\")
                    ans = max(alexSum + totalCounts, ans)
                # print(f\"alexTurn = {alexTurn} index = {index} x = {x} M = {max(m, x + 1)} ans = {alexSum + totalCounts}\")

            else:
                ans = sys.maxsize
                for x in range(2*m):
                    if (index + x == len(self.piles)):
                        break
                    totalCounts += self.piles[index + x]
                    alexSum = Util(not alexTurn, index + x + 1, max(m, x+1))
                    ans = min(alexSum, ans)
                # print(f\"alexTurn = {alexTurn} index = {index} x = {x} M = {max(m, x + 1)} ans = {alexSum + totalCounts}\")
            self.dp[turn][index][m] = ans
            return ans
        self.dp = [-1]*2
        for i in range(2):
            self.dp[i] = [-1]*len(piles)
            for j in range(len(piles)):
                self.dp[i][j] = [-1] * len(piles)
                
        self.piles = piles
        return Util(True, 0, 1)
        
