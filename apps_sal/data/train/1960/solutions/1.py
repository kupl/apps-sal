class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = collections.deque(list(range(1, m + 1)))

        res = []

        for q in queries:
            res.append(P.index(q))
            del P[res[-1]]
            P.appendleft(q)
            # print(P)

        return res
