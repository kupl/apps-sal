class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        ans = 0
        MOD = 10**9 + 7

        def fun(ind, arr, rem, target):
            if (ind, rem) in dp:
                return dp[ind, rem]
            cnt = 0
            if ind == target:
                cnt += 1

            for i, val in enumerate(arr):
                if i == ind:
                    continue
                if abs(arr[ind] - val) <= rem:
                    cnt += fun(i, arr, rem - abs(arr[ind] - val), target)
            dp[ind, rem] = cnt % (10**9 + 7)
            return dp[ind, rem]
        dp = {}
        return fun(start, locations, fuel, finish)
