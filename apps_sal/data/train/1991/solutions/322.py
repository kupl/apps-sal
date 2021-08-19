class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def count(n):
            if n == 0:
                return 1
            ans = 0
            for i in range(1, n + 1):
                ans += count(n - i)
            return ans

        # print(count(0), count(1), count(2), count(3))

        dct = defaultdict(int)

        for i, l in enumerate(locations):
            dct[l] = i

        start_location, end_location = locations[start], locations[finish]
        # locations.sort()
        start_idx, end_idx = dct[start_location], dct[end_location]

        @lru_cache(None)
        def dfs(idx, fuel):
            # print(idx, fuel)
            ans = 0
            if idx == end_idx:
                ans += 1
            for i, l in enumerate(locations):
                if i != idx and abs(l - locations[idx]) <= fuel:
                    ans += dfs(i, fuel - abs(l - locations[idx]))
            return ans % mod

        return dfs(start_idx, fuel)
