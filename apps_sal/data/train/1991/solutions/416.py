class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def routes(From, fuel):

            if fuel < 0:
                return 0

            if (From, fuel) in cache:
                return cache[(From, fuel)]

            ways = 0
            if From == finish and fuel >= 0:
                ways += 1
            for city in range(len(locations)):
                if city != From:
                    ways += routes(city, fuel - abs(locations[city] - locations[From]))
            cache[(From, fuel)] = ways % mod
            return cache[(From, fuel)] % mod

        mod = 10**9 + 7
        cache = {}
        return routes(start, fuel)
