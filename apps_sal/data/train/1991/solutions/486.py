class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        lookup = {}

        def count(curr, fuel, lookup):
            if fuel < 0:
                return 0
            key = str(curr) + '@' + str(fuel)
            if key in lookup:
                return lookup[key]
            else:
                ret = 0
                if curr == finish:
                    ret = 1
                for i in range(len(locations)):
                    if i != curr and fuel >= abs(locations[curr] - locations[i]):
                        ret += count(i, fuel - abs(locations[i] - locations[curr]), lookup)
                lookup[key] = ret % 1000000007
                return lookup[key]
        return count(start, fuel, lookup)
