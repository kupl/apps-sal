class Solution:

    def playerGame(self, pos, piles, player1, M, memo):
        optionsCount = min(len(piles) - pos, 2 * M)
        resultPlayer1 = 0
        resultPlayer2 = 0
        for i in range(pos, pos + optionsCount):
            X = i - pos + 1
            stonesCount = 0
            for j in range(pos, i + 1):
                stonesCount += piles[j]
            combination = (i + 1, not player1, max(M, X))
            if combination in memo:
                (count1, count2) = memo[combination]
            else:
                (count1, count2) = self.playerGame(i + 1, piles, not player1, max(M, X), memo)
                memo[combination] = [count1, count2]
            if player1:
                if stonesCount + count1 > resultPlayer1:
                    resultPlayer1 = stonesCount + count1
                    resultPlayer2 = count2
            elif stonesCount + count2 > resultPlayer2:
                resultPlayer1 = count1
                resultPlayer2 = stonesCount + count2
        return (resultPlayer1, resultPlayer2)

    def stoneGameII(self, piles: List[int]) -> int:
        M = 1
        player1 = True
        memo = {}
        pos = 0
        return self.playerGame(pos, piles, player1, M, memo)[0]
