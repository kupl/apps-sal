class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dfs(x, y, f):
            if abs(A[x] - A[y]) > f:
                print((x, y, f, 0))
                return 0
            ret = 0
            if abs(A[x] - A[y]) <= f:
                ret += 1
            for mid in range(n):
                g = abs(A[mid] - A[x]) + abs(A[mid] - A[y])
                if mid == x or g > f:
                    continue
                ret += dfs(mid, y, f - abs(A[mid] - A[x]))
                if mid == y:
                    ret -= 1
                ret %= MOD
            return ret

        A = locations
        n = len(A)
        MOD = 10 ** 9 + 7
        return dfs(start, finish, fuel)
