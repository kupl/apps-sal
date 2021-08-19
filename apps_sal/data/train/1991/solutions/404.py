class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        memo = dict()

        def backtrack(n, k):
            if k < 0:
                return 0
            if k == 0:
                return int(n == finish)
            key = (n, k)
            if key not in memo:
                memo[key] = int(n == finish)
                for nei in range(len(locations)):
                    if nei != n:
                        memo[key] += backtrack(nei, k - abs(locations[n] - locations[nei])) % 1000000007
            return memo[key]
        return backtrack(start, fuel) % 1000000007
