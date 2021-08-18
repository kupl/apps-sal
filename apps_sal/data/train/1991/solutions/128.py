class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        modulo = 10 ** 9 + 7
        n = len(locations)
        start_pos, finish_pos = locations[start], locations[finish]
        locations.sort()
        start = locations.index(start_pos)
        finish = locations.index(finish_pos)

        @lru_cache(None)
        def dp(cur, fuel):
            res = 0
            if cur == finish:
                res += 1
            for nxt in range(cur + 1, n):
                if nxt < 0 or nxt >= n:
                    continue
                if abs(locations[nxt] - locations[cur]) > fuel:
                    break
                res += dp(nxt, fuel - abs(locations[nxt] - locations[cur]))
            for nxt in range(cur - 1, -1, -1):
                if nxt < 0 or nxt >= n:
                    continue
                if abs(locations[nxt] - locations[cur]) > fuel:
                    break
                res += dp(nxt, fuel - abs(locations[nxt] - locations[cur]))
            return res % modulo
        return dp(start, fuel)
