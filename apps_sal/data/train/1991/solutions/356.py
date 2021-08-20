class Solution:

    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[-1] * (len(locations) + 1) for _ in range(fuel + 1)]

        def recur(st, ed, f):
            if f < 0:
                return 0
            if dp[f][st] != -1:
                return dp[f][st]
            total = 0
            for i in range(len(locations)):
                if i != st:
                    total += recur(i, ed, f - abs(locations[st] - locations[i]))
            if st == ed:
                answer = (total + 1) % MOD
            else:
                answer = total % MOD
            dp[f][st] = answer
            return answer
        recur(start, finish, fuel)
        return dp[fuel][start]
