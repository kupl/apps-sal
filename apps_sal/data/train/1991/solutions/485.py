from functools import lru_cache


def count_routes(locations, start, finish, fuel):
    M = 10 ** 9 + 7
    dp = [[0] * len(locations) for _ in range(0, fuel + 1)]
    dp[fuel][start] = 1
    for f in range(fuel, -1, -1):
        for (c, c_loc) in enumerate(locations):
            for (d, d_loc) in enumerate(locations):
                if d == c:
                    continue
                gas = abs(c_loc - d_loc)
                if f + gas <= fuel:
                    dp[f][c] = dp[f][c] + dp[f + gas][d]
    return sum((dp[f][finish] for f in range(0, fuel + 1))) % M


class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        return count_routes(locations, start, finish, fuel)
