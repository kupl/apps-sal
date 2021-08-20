class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i + 1 for i in range(m)]
        res = []
        for q in queries:
            i = P.index(q)
            res.append(i)
            P = [q] + P[:i] + P[i + 1:]
        return res
