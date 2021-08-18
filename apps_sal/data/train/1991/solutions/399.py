class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if abs(locations[start] - locations[finish]) > fuel:
            return 0
        d = {}

        def findcombo(current_pos, rem_fuel):
            count = 0
            if (current_pos, rem_fuel) in d:
                return d[(current_pos, rem_fuel)]
            if rem_fuel >= 0 and current_pos == finish:
                count += 1
            if rem_fuel > 0:
                for i in range(0, len(locations)):
                    if i != current_pos:
                        balance = abs(locations[current_pos] - locations[i]) + abs(locations[current_pos] - locations[finish])
                        if balance >= 0:
                            count += findcombo(i, rem_fuel - abs(locations[current_pos] - locations[i]))
            d[(current_pos, rem_fuel)] = count
            return count
        c = findcombo(start, fuel)
        return c % 1000000007
