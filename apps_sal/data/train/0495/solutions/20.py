class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        DP
        O(N * SUM//2)

        As this problem is equal to min diff between dividing arr into two groups, sse dp to store sum//2 and see if we can reach it
        '''

        total = sum(stones)

        dp = [[None for _ in range(((total // 2) + 1))] for _ in range(len(stones))]

        for num in range((total // 2) + 1):
            if stones[0] <= num:
                dp[0][num] = stones[0]
            else:
                dp[0][num] = 0

        for index in range(1, len(stones)):
            for num in range((total // 2) + 1):
                if stones[index] <= num:
                    take = stones[index] + dp[index - 1][num - stones[index]]
                    dp[index][num] = max(take, dp[index - 1][num])
                else:
                    dp[index][num] = dp[index - 1][num]

        # print(dp)

        return total - dp[-1][-1] - dp[-1][-1]
