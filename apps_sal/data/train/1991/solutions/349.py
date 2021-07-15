class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.locations = locations
        self.nr = [[0] * (fuel + 1) for _ in locations]
        self.evaluated = [[False] * (fuel + 1) for _ in locations]
        for i in range(len(locations) - 1):
            self.nr[i][0] = 0
            self.evaluated[i][0] = True
        for i in range(fuel + 1):
            self.nr[finish][i] = 1
        self.evaluated[finish][0] = True
        x = self.num_routes(start, finish, fuel)
        return x
        
    def num_routes(self, current_city, end, current_fuel):
        # add num_routes for (places, fuel) states that can be travelled to with current fuel.
        # print('Start eval:', current_city, current_fuel)
        if self.evaluated[current_city][current_fuel]:
            # print('Applied old eval:', current_city, current_fuel, self.nr[current_city][current_fuel])
            return self.nr[current_city][current_fuel]
        cur_nr = self.nr[current_city][current_fuel]
        for target_city in range(len(self.locations)):
            if target_city == current_city:
                continue
            remaining_fuel = current_fuel - max(self.locations[current_city] - self.locations[target_city], self.locations[target_city] - self.locations[current_city])
            if remaining_fuel >= 0:
                cur_nr += self.num_routes(target_city, end, remaining_fuel)
        
        cur_nr = cur_nr % (10**9 + 7)
        self.nr[current_city][current_fuel] = cur_nr
        self.evaluated[current_city][current_fuel] = True
        # print(location, current_fuel, cur_nr)
        # print('Fin eval:', current_city, current_fuel, cur_nr)
        return cur_nr
