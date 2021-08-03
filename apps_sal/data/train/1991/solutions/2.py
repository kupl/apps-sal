class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        count = 0
        mod = 10**9 + 7
        n = len(locations)
        s_l = locations[start]
        f_l = locations[finish]
        locations.sort()
        start = locations.index(s_l)
        finish = locations.index(f_l)

        import functools

        @functools.lru_cache(None)
        def DFS(cur_city, cur_fuel):
            if cur_fuel < abs(locations[cur_city] - locations[finish]):
                return 0
            i = bisect.bisect_left(locations, locations[cur_city] - cur_fuel)
            j = min(n - 1, bisect.bisect_left(locations, locations[cur_city] + cur_fuel))

            return (1 * (cur_city == finish) + sum(DFS(nxt, cur_fuel - abs(locations[cur_city] - locations[nxt])) for nxt in range(i, j + 1) if (nxt != cur_city))) % mod

        return DFS(start, fuel)
