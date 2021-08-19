class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        array = [[0 for i in range(len(locations))] for j in range(fuel + 1)]
        for fuel_idx in range(len(array)):
            array[fuel_idx][finish] = 1
        for fuel_max in range(1, len(array)):
            for loc in range(len(array[0])):
                route_count = array[fuel_max][loc]
                for loc_idx in range(len(array[0])):
                    if loc_idx == loc:
                        continue
                    fuel_res = fuel_max - abs(locations[loc] - locations[loc_idx])
                    if fuel_res < 0:
                        continue
                    route_count += array[fuel_res][loc_idx]
                array[fuel_max][loc] = route_count
        return array[fuel][start] % (10 ** 9 + 7)
