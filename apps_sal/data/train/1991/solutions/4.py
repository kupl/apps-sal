class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if (not locations) or fuel <= 0:
            return 0

        route_dict = {f: {} for f in range(fuel, -1, -1)}
        route_dict[fuel][start] = 1

        total_route = 0

        for f in range(fuel, 0, -1):
            for i, num_route in list(route_dict[f].items()):
                for j in range(len(locations)):
                    if j != i:
                        d = abs(locations[i] - locations[j])
                        if f >= d:
                            if not j in route_dict[f - d]:
                                route_dict[f - d][j] = num_route
                            else:
                                route_dict[f - d][j] += num_route

        for f in route_dict:
            if finish in route_dict[f]:
                total_route += route_dict[f][finish]

        return total_route % (10**9 + 7)
