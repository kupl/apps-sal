from collections import defaultdict
from sortedcontainers import SortedSet


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        def getCeil(a, v):
            if not a:
                return None
            b = a.bisect_right(v)

            if b == 0:
                if a[b] >= v:
                    return a[b]
                return None
            if b == len(a):
                return None
            return a[b]

        res = [0] * len(rains)
        zeros = SortedSet()
        m = {}
        for i, val in enumerate(rains):
            if val == 0:
                zeros.add(i)
            else:
                if val in m:
                    n = getCeil(zeros, m[val])
                    print(n)
                    if not n:
                        return []
                    res[n] = val
                    zeros.remove(n)
                res[i] = -1
                m[val] = i
        for i in zeros:
            res[i] = 1
        return res
