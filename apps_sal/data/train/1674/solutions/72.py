class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        self.arr = piles
        self.dp = {}
        ans = self.helper(0, 1, 1)
        print(self.dp)
        return ans

    def helper(self, i, m, turn):
        if i >= len(self.arr):
            return 0
        if (i, m, turn) in self.dp:
            return self.dp[i, m, turn]
        if turn:
            ans = []
            for x in range(2 * m):
                tmp = sum(self.arr[i:i + x + 1]) + self.helper(i + x + 1, max(x + 1, m), 0)
                ans.append(tmp)
            self.dp[i, m, turn] = max(ans)
            return self.dp[i, m, turn]
        else:
            ans = []
            for x in range(2 * m):
                tmp = self.helper(i + x + 1, max(x + 1, m), 1)
                ans.append(tmp)
            self.dp[i, m, turn] = min(ans)
            return self.dp[i, m, turn]
