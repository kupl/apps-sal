class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @functools.lru_cache(None)
        def get(start=start, fuel=fuel):
            if fuel < abs(locations[start] - locations[finish]):
                return 0

            to_ret = 1 if start == finish else 0
            for p in range(len(locations)):
                if p == start:
                    continue
                to_ret += get(p, fuel=max(0, fuel - abs(locations[start] - locations[p])))
            return to_ret % (10**9 + 7)

        return get()
