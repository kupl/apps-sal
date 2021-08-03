class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        startFuel = fuel
        memo = [[-1 for f in range(fuel + 1)] for l in range(len(locations))]

        def recurse(start, fuel, memo):

            # Base case: Not enough fuel to get to the destination
            numRoutes = 0
            if fuel >= 0:

                # Memoization: We've seen this problem before
                if memo[start][fuel] != -1:

                    numRoutes = memo[start][fuel]

                else:

                    # Test: If we have reached the finish, we have completed a valid route... but we still want to continue on if we have more fuel :P
                    if start == finish:
                        numRoutes += 1

                    # Recurse: Try to move to all other cities
                    for nextCity in range(0, len(locations)):
                        if nextCity != start:
                            numRoutes += recurse(nextCity, fuel - abs(locations[nextCity] - locations[start]), memo)

                    # Memoize: Save off the result of our computation
                    memo[start][fuel] = numRoutes

            # Return the number of routes that get us from start to finsh with the given amount of fuel
            return numRoutes

        return recurse(start, fuel, memo) % ((10**9) + 7)
