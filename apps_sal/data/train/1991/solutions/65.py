class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        return foo(locations, start, finish, fuel)

from functools import lru_cache
def foo(cities, start, end, f):
    n = len(cities)
    @lru_cache(maxsize=None)
    def bar(i, f):
        rv = 0
        if f < 0:
            return 0
        if i == end:
            rv += 1
        return rv + sum(bar(j, f - abs(cities[j] - cities[i])) for j in range(n) if i != j)
    return bar(start, f) % (10**9 + 7)
