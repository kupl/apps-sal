def count_all_possible_routes(locations, start, finish, fuel):
    loc_count = len(locations)
    dp_store = [[-1] * (fuel + 1) for loc in range(loc_count)]

    # print('*' * 80)
    # print('iron man dp_store', dp_store)

    def count_all_possible_routes_recur(curr_loc, rem_fuel):
        if rem_fuel < 0:
            return 0
        if dp_store[curr_loc][rem_fuel] > -1:
            return dp_store[curr_loc][rem_fuel]
        ans = 0
        if curr_loc == finish:
            ans += 1
        for city, pos in enumerate(locations):
            if city == curr_loc:
                continue
            ans += count_all_possible_routes_recur(
                city, rem_fuel - (abs(pos - locations[curr_loc])))
        dp_store[curr_loc][rem_fuel] = ans
        return ans

    return count_all_possible_routes_recur(start, fuel) % ((10 ** 9) + 7)


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        return count_all_possible_routes(locations, start, finish, fuel)
