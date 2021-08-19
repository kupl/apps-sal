class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        count = 0
        mod = 10 ** 9 + 7
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
            if cur_city == finish:
                c = 1
            else:
                c = 0
            i = bisect.bisect_left(locations, locations[cur_city] - cur_fuel)
            j = min(n - 1, bisect.bisect_left(locations, locations[cur_city] + cur_fuel))
            for nxt in range(i, cur_city):
                c += DFS(nxt, cur_fuel - abs(locations[cur_city] - locations[nxt]))
            for nxt in range(cur_city + 1, j + 1):
                c += DFS(nxt, cur_fuel - abs(locations[cur_city] - locations[nxt]))
            return c % mod
        return DFS(start, fuel) % mod
