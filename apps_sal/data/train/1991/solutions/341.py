class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        startFuel = fuel
        memo = [[-1 for f in range(fuel + 1)] for l in range(len(locations))]

        def recurse(start, fuel, memo):

            numRoutes = 0
            if fuel >= 0:

                if memo[start][fuel] != -1:

                    numRoutes = memo[start][fuel]

                else:

                    if start == finish:
                        numRoutes += 1

                    for nextCity in range(0, len(locations)):
                        if nextCity != start:
                            numRoutes += recurse(nextCity, fuel - abs(locations[nextCity] - locations[start]), memo)

                    memo[start][fuel] = numRoutes

            return numRoutes

        return recurse(start, fuel, memo) % ((10**9) + 7)
