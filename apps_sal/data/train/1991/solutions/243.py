class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        pos_start = locations[start]
        pos_finish = locations[finish]
        locations.sort()
        start = locations.index(pos_start)
        finish = locations.index(pos_finish)

        @lru_cache(maxsize=None)
        def find(start, fuel):
            count = 0
            if abs(start - finish) == 1 and fuel == abs(locations[start] - locations[finish]):
                return 1
            if locations[start] == locations[finish]:
                count += 1
            if fuel >= abs(locations[start] - locations[finish]):
                for i in range(start - 1, -1, -1):
                    if abs(locations[start] - locations[i]) + abs(locations[i] - locations[finish]) <= fuel:
                        count += find(i, fuel - abs(locations[start] - locations[i]))
                    else:
                        break
                for j in range(start + 1, len(locations)):
                    if abs(locations[start] - locations[j]) + abs(locations[j] - locations[finish]) <= fuel:
                        count += find(j, fuel - abs(locations[start] - locations[j]))
                    else:
                        break
            return count
        return find(start, fuel) % MOD
