class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0] * 201 for i in range(n)]
        start0 = start
        fuel0 = fuel
        for fuel in range(fuel0 + 1):
            for start in range(n):
                temp = 0
                for mid in range(n):
                    if start == mid:
                        continue
                    dis = abs(locations[mid] - locations[start])
                    if dis <= fuel:
                        temp = temp + dp[mid][fuel - dis]
                if start == finish:
                    temp = temp + 1
                dp[start][fuel] = temp % (10 ** 9 + 7)
        return dp[start0][fuel0]
