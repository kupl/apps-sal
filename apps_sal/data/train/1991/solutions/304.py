class Solution:

    def countRoutes(self, l: List[int], start: int, fin: int, fuel: int) -> int:
        (a, b, i) = (l[start], l[fin], 0)
        while i < len(l):
            if abs(l[i] - a) + abs(l[i] - b) > fuel:
                del l[i]
            else:
                i += 1
        if not l:
            return 0
        n = len(l)
        (start, fin) = (l.index(a), l.index(b))

        @lru_cache(None)
        def dfs(i: int, f: int) -> int:
            return 0 if f < 0 else (1 if i == fin else 0) + sum((0 if i == j else dfs(j, f - abs(l[j] - l[i])) for j in range(len(l))))
        return dfs(start, fuel) % 1000000007
