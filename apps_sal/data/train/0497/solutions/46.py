class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        table = [[] for i in range(n)]
        for i in range(n):
            table[i] = [startTime[i], endTime[i], profit[i]]
        table.sort(key=lambda x: x[1])
        print(table)

        def find(table, x):
            l = 0
            h = n - 1
            ans = -1
            while l <= h:
                m = (l + h) // 2
                if table[m][1] == x:
                    return m
                if table[m][1] < x:
                    ans = m
                    l = m + 1
                else:
                    h = m - 1
            return ans
        dp = [0] * n
        dp[0] = table[0][2]
        mx = 0
        for i in range(1, n):
            x = table[i][0]
            loca = find(table, x)
            if loca >= 0:
                ans = table[i][2] + dp[loca]
            else:
                ans = table[i][2]
            dp[i] = max(ans, dp[i - 1])
        print(dp)
        return max(dp)
