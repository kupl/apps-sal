class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        def helper(c, f):
            if (c, f) not in d:
                t = c == finish
                if f > 0:
                    for i in range(len(locations)):
                        u = abs(locations[i] - locations[c])
                        if i != c and u <= f:
                            t += helper(i, f - u)
                d[c, f] = t % 1_000_000_007
            return d[c, f]
        d = {}
        return helper(start, fuel)
