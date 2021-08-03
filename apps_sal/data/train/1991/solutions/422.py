class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @functools.lru_cache(maxsize=None)
        def recurse(locations, start, finish, fuel):
            output = 0
            if fuel < 0:
                return 0
            if start == finish:
                output += 1
            for i in range(len(locations)):
                if i != start:
                    output += recurse(locations, i, finish, fuel - abs(locations[i] - locations[start]))
            return output
        return recurse(tuple(locations), start, finish, fuel) % (10**9 + 7)
