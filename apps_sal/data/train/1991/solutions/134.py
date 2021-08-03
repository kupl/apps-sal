class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # 使用DP记忆数据，可以在时间复杂度不那么高的前提下解决问题
        # dp作为缓存数据，存储了到达当前地点和剩余燃料可以到达终点的路径数
        # dp的行id为地点
        # dp的列id为剩余燃料
        dp = [[-1] * (fuel + 1) for _ in range(len(locations))]

        def route(st, ed, fuel):
            if dp[st][fuel] > -1:
                return dp[st][fuel]
            res = 0 if st != ed else 1
            for i in range(len(locations)):
                if i != st and fuel - abs(locations[st] - locations[i]) >= 0:
                    res += route(i, ed, fuel - abs(locations[st] - locations[i]))
            dp[st][fuel] = res % 1000000007
            return dp[st][fuel]
        # print(dp)
        return route(start, finish, fuel)
