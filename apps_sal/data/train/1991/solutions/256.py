class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        DP = {}

        def f(i, fuel):
            # Returns number of paths to finish starting from `i` and `fuel`
            if fuel < 0:
                return 0
            if (i, fuel) in DP:
                return DP[i, fuel]
            count = 0
            if i == finish:
                count += 1
            for j in range(len(locations)):
                if i != j:
                    count = (count + f(j, fuel - abs(locations[i] - locations[j]))) % MOD
            DP[i, fuel] = count
            return count
        return f(start, fuel)
