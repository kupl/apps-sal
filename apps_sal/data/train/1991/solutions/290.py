import heapq as hq


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start_loc = locations[start]
        finish_loc = locations[finish]
        locations = sorted(locations)
        start = locations.index(start_loc)
        finish = locations.index(finish_loc)

        pushed = set([(fuel, start, 1), (start, fuel, -1)])
        h = [(-fuel, start, 1), (-fuel, start, -1)]
        routes = {(start, fuel, 1): 1, (start, fuel, -1): 1}
        count = 0
        if start == finish:
            count = 1

        while len(h) > 0:
            neg_fuel, st, di = hq.heappop(h)
            ed = st + di
            inc = routes[(st, -neg_fuel, di)]
            while True:
                if ed < 0 or ed > len(locations) - 1:
                    break
                new_fuel = - neg_fuel - abs(locations[ed] - locations[st])
                if new_fuel < 0:
                    break
                if (new_fuel, ed, -di) not in pushed:
                    pushed.add((new_fuel, ed, -di))
                    routes[(ed, new_fuel, -di)] = inc
                    hq.heappush(h, (-new_fuel, ed, -di))
                else:
                    routes[(ed, new_fuel, -di)] += inc
                if ed == finish:
                    count += inc
                ed += di
                inc *= 2
        return count % 1000000007
