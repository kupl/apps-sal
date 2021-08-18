class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        memo = {}
        return self.dp(locations, start, finish, fuel, memo)

    def dp(self, locations, i, finish, fuel, memo) -> int:
        if fuel < 0:
            return 0

        if (i, fuel) in memo:
            return memo[(i, fuel)]

        res = 0

        if i == finish:
            res += 1

        for j in range(len(locations)):
            if i == j:
                continue

            res += self.dp(locations, j, finish, fuel - abs(locations[i] - locations[j]), memo)

        memo[(i, fuel)] = res % (10 ** 9 + 7)
        return memo[(i, fuel)]
