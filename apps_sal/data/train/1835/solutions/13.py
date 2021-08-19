class Solution:

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        @functools.lru_cache(maxsize=128, typed=False)
        def check(n, k, s):
            rtv = []
            if n == 0:
                return []
            rtv = []
            for i in range(10):
                if abs(i - s) == k:
                    r1 = check(n - 1, k, i)
                    if r1:
                        for r in r1:
                            rtv.append([i] + r)
                    else:
                        rtv.append([i])
            return rtv
        rtv = []
        for i in range(1, 10):
            r0 = check(n - 1, k, i)
            for r in r0:
                t = i
                for c in r:
                    t = t * 10 + c
                rtv.append(t)
        return rtv
