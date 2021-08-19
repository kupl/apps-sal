from collections import deque


class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = deque(list(range(1, m + 1)))
        result = []
        for q in queries:
            for (i, n) in enumerate(p):
                if q == n:
                    p.remove(n)
                    p.appendleft(n)
                    result.append(i)
                    break
        return result
