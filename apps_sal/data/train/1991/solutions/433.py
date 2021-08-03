class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start, finish = locations[start], locations[finish]
        d = {}
        for f in range(fuel + 1):
            for loc in locations:
                d[(loc, f)] = sum(d[(new_loc, f - abs(loc - new_loc))] for new_loc in locations if f >= abs(loc - new_loc) and loc != new_loc) + (loc == finish) * (f >= 0)
        return d[start, fuel] % (10**9 + 7)
