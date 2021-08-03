# class Solution:
#     def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
#         if fuel < 0:
#             return 0

#         result = 0
#         if start == finish:
#             result = 1

#         for i in range(len(locations)):
#             if i != start:
#                 result = (result + self.countRoutes(locations, i, finish, fuel - abs(i - start))) % 1000000007
#         return result
class Solution:
    def dp(self, A, curr, e, fuel, dp):
        mod = 10 ** 9 + 7
        if fuel < 0:
            return 0
        if dp[curr][fuel] != -1:
            return dp[curr][fuel]

        ans = 1 if curr == e else 0
        for nxt in range(len(A)):
            if nxt != curr:
                ans += self.dp(A, nxt, e, fuel - abs(A[curr] - A[nxt]), dp)
                ans %= mod

        dp[curr][fuel] = ans
        return ans

    def countRoutes(self, A: List[int], s: int, e: int, fuel: int) -> int:
        if not A:
            return 0
        n = len(A)
        dp = [[-1] * (fuel + 1) for _ in range(n)]
        return self.dp(A, s, e, fuel, dp)
