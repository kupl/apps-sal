class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if fuel < abs(locations[start] - locations[finish]):
            return 0
        mask = int(1e9 + 7)
        table = [[0] * len(locations) for i in range(fuel+1)]
        table[fuel][start] = 1
        for f in reversed(list(range(1, fuel + 1))):
            for loc1 in range(len(locations)):
                if table[f][loc1] == 0:
                    continue
                for loc2 in range(len(locations)):
                    if loc2 == loc1:
                        continue
                    fuel_required = abs(locations[loc1] - locations[loc2])
                    if fuel_required <= f:
                        table[f-fuel_required][loc2] += table[f][loc1]
        return sum([table[f][finish] for f in range(fuel+1)]) % mask

