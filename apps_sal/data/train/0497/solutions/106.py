class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        stack = [0 for _ in range(n)]
        for i in range(len(startTime)):
            stack[i] = [startTime[i], endTime[i], profit[i]]
        stack = sorted(stack, key=lambda x: x[1])
        print(stack)
        dp = [[0, 0]]
        for (s, e, p) in stack:
            idx = self.binarySearch(dp, s)
            if dp[idx][1] + p > dp[-1][1]:
                dp.append([e, dp[idx][1] + p])
        return dp[-1][1]

    def binarySearch(self, dp, s):
        (i, j) = (0, len(dp))
        while i < j:
            mid = i + (j - i) // 2
            if dp[mid][0] == s:
                return mid
            elif dp[mid][0] > s:
                j = mid
            else:
                i = mid + 1
        if i == len(dp):
            return i - 1
        elif dp[i][0] > s:
            return i - 1
        else:
            return i
