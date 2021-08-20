class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1, m + 1)]
        result = []
        for q in queries:
            result.append(P.index(q))
            P.remove(q)
            P.insert(0, q)
        return result
