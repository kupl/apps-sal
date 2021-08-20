class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def recurse(index, fuel, finish):
            paths = 0
            if fuel < 0:
                return 0
            if index == finish:
                paths += 1
            if dp[index][fuel] != -1:
                return dp[index][fuel]
            for i in range(len(locations)):
                if i == index:
                    continue
                paths += recurse(i, fuel - abs(locations[i] - locations[index]), finish)
            dp[index][fuel] = paths % (pow(10, 9) + 7)
            return paths
        dp = [[-1 for i in range(fuel + 1)] for j in range(len(locations))]
        totalpaths = recurse(start, fuel, finish) % (pow(10, 9) + 7)
        return totalpaths
