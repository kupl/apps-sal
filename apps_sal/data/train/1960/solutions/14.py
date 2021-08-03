class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        out = []
        P = [i for i in range(1, m + 1)]
        for i in queries:
            #num = P.index(i)
            out.append(P.index(i))
            P.insert(0, P.pop(P.index(i)))
        return out
