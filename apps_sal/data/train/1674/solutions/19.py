class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        s = sum(piles[:])
        memo = [[-sys.maxsize for i in range(2 * n)] for j in range(n)]

        def DFS(m: int, index: int) -> int:
            if memo[m][index] != -sys.maxsize:
                return memo[m][index]
            if index >= n:
                return 0
            score = -sys.maxsize
            take = min(n - 1, index + 2 * m - 1)

            for i in range(index, take + 1):
                score = max(score, sum(piles[index:i + 1]) - DFS(max(i - index + 1, m), i + 1))
                # print(index,i+1,sum(piles[index:i+1]),score)
            memo[m][index] = score
            return score

        return (DFS(1, 0) + s) // 2
