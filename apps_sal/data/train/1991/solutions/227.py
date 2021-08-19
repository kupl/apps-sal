class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        memo = {}

        def f(i, fuel_remain):
            if (i, fuel_remain) in memo:
                return memo[i, fuel_remain]
            total = 0
            for j in range(len(locations)):
                if i == j or abs(locations[j] - locations[i]) > fuel_remain:
                    continue
                if j == finish:
                    total += 1
                total += f(j, fuel_remain - abs(locations[j] - locations[i]))
            memo[i, fuel_remain] = total
            return total % (10 ** 9 + 7)
        return f(start, fuel) + (1 if start == finish else 0)
