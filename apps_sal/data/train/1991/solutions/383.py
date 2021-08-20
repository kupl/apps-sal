class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def solve(end, fuel):
            nonlocal n, start
            if fuel == 0:
                if end == start:
                    return 1
                else:
                    return 0
            ans = 0
            for i in range(n):
                if i != end and abs(locations[i] - locations[end]) <= fuel:
                    ans += solve(i, fuel - abs(locations[i] - locations[end]))
            return ans
        ans = 0
        for i in range(fuel + 1):
            ans += solve(finish, i)
        return ans % mod
