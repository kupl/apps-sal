class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        l = len(locations)
        dp = [[['x' for _ in range(l)] for _ in range(l)] for _ in range(fuel + 1)]

        def find_way(s, f, fu):
            if fu < 0:
                return 0
            if dp[fu][s][f] != 'x':
                return dp[fu][s][f]
            r = 1 if s == f else 0
            for i in range(l):
                if i != s:
                    r += find_way(i, f, fu - abs(locations[s] - locations[i]))
            dp[fu][s][f] = r
            return r

        return find_way(start, finish, fuel) % (10 ** 9 + 7)
