class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}
        M = 1e9 + 7

        def go(now, f):
            if (now, f) in dp:
                return dp[(now, f)]
            if f < 0:
                return 0
            if now == finish:
                dp[(now, f)] = 1
                for i, v in enumerate(locations):
                    if i != now and f - abs(locations[now] - v) >= 0:
                        dp[(now, f)] += go(i, f - abs(locations[now] - v))
                dp[(now, f)] %= M
                return dp[(now, f)]
            dp[(now, f)] = 0
            for i, v in enumerate(locations):
                if i != now and f - abs(locations[now] - v) >= 0:
                    dp[(now, f)] += go(i, f - abs(locations[now] - v))
            dp[(now, f)] %= M
            return dp[(now, f)]
        return int(go(start, fuel))
