class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        d = {}
        n = len(locations)
        st, fi = locations[start], locations[finish]
        locations.sort()
        for i in range(n):
            d[locations[i]] = i

        dp = [[[0 for f in range(fuel + 1)] for _ in range(n)] for __ in range(n)]
        for i in range(n):
            dp[i][i][0] = 1

        def helper(i, j, f):
            nonlocal dp

            if dp[i][j][f] != 0:
                return dp[i][j][f]
            if abs(locations[i] - locations[j]) > f:
                return 0
            if i == j:
                dp[i][j][f] += 1

            for k in range(i - 1, -1, -1):
                if abs(locations[k] - locations[i]) > f:
                    break
                dp[i][j][f] += helper(k, j, f - abs(locations[k] - locations[i]))
            for k in range(i + 1, n):
                if abs(locations[k] - locations[i]) > f:
                    break
                dp[i][j][f] += helper(k, j, f - abs(locations[k] - locations[i]))
            return dp[i][j][f]

        return helper(d[st], d[fi], fuel) % (10 ** 9 + 7)
