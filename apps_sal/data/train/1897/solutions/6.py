class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        dp = [0] * len(arr)
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            dp[i] = dp[i - 1] ^ arr[i]
        res = []
        for i in range(len(queries)):

            if queries[i][0] > 0:
                res.append(dp[queries[i][0] - 1] ^ dp[queries[i][1]])
            else:
                res.append(dp[queries[i][1]])

        return res
