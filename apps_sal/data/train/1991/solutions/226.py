class Solution:
    def countRoutes(self, A: List[int], start: int, end: int, fuel: int) -> int:

        mod = 10 ** 9 + 7

        def cost(a, b): return abs(A[a] - A[b])

        @functools.lru_cache(None)
        def route(start, fuel):
            nonlocal end

            if fuel < 0:
                return 0

            r = 1 if start == end else 0

            for i in range(len(A)):

                if i == start:
                    continue

                r += route(i, fuel - cost(start, i)) % mod

            return r % mod

        answer = route(start, fuel)
        return answer
