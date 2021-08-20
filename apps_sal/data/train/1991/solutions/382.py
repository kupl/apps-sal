class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        cache = dict()

        def helper(i, f):
            if f < 0:
                return 0
            if (i, f) not in cache:
                count = 1 if i == finish else 0
                for j in range(len(locations)):
                    if i != j:
                        count += helper(j, f - abs(locations[i] - locations[j]))
                cache[i, f] = count
            return cache[i, f]
        return helper(start, fuel) % 1000000007
