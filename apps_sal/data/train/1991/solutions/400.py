class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        def count(start, fuel):
            if fuel < 0:
                return 0

            if (start, fuel) in memo:
                return memo[(start, fuel)]

            s = 0  # sum
            if start == finish:
                s += 1
            for i in range(len(locations)):
                if i != start:
                    s += count(i, fuel - abs(locations[i] - locations[start]))
            memo[(start, fuel)] = s
            return s

        memo = {}
        return count(start, fuel) % (10**9 + 7)
