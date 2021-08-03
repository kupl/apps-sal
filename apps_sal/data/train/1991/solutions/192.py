class Solution:
    def countRoutes(self, L: List[int], start: int, finish: int, fuel: int) -> int:

        def cost(x, y): return abs(L[x] - L[y])
        ways = {}

        def numWays(s, f):
            if (s, f) not in ways:

                if f < cost(s, finish):
                    return 0

                total = 0
                for u in range(len(L)):
                    if u != s:
                        total += numWays(u, f - cost(s, u))

                ways[(s, f)] = total + (s == finish)
            return ways[(s, f)]

        return numWays(start, fuel) % (10 ** 9 + 7)
