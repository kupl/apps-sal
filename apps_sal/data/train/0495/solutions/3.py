class Solution:
    def lastStoneWeightII(self, arr: List[int]) -> int:
        #0/1 knapsack
        upperBound = sum(arr)//2
        #initialize the dp -> row means use up to ith value, row means the upper bound value 
        dp = [[0 for i in range(upperBound+1)] for j in range(len(arr))]

        #fill in the dp
        #base case when col == 0 -> the upper bound is 0, so the max val is 0 
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                #take i or not
                if(arr[i] <= j):
                    dp[i][j] = max(dp[i-1][j-arr[i]] + arr[i], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return sum(arr) - 2*dp[-1][-1]
