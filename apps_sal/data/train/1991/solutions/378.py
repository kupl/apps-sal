class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        neighbors = defaultdict(list)
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                if abs(locations[i] - locations[j]) <= fuel:
                    neighbors[i].append((j, abs(locations[i] - locations[j])))
                    neighbors[j].append((i, abs(locations[i] - locations[j])))

        @lru_cache(None)
        def helper(location, fuel_remaining):
            sum = 0
            if fuel_remaining < 0:
                return 0
            if location == finish:
                sum += 1
            for (neighbor, cost) in neighbors[location]:
                sum += helper(neighbor, fuel_remaining - cost)
            return sum
        return helper(start, fuel) % (10 ** 9 + 7)
