class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        seen = {}

        def cost(i, j):
            return abs(locations[i] - locations[j])

        def dfs(n, f):
            if f < 0:
                return 0
            if f < cost(n, finish):
                return 0
            if '{}_{}'.format(n, f) in seen:
                return seen['{}_{}'.format(n, f)]
            ans = int(n == finish)
            for next_n in range(len(locations)):
                if next_n != n:
                    ans += dfs(next_n, f - cost(n, next_n))
            seen['{}_{}'.format(n, f)] = ans % (10 ** 9 + 7)
            return ans % (10 ** 9 + 7)
        return dfs(start, fuel)
