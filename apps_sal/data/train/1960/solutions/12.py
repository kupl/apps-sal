class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        retIndexlist = []
        p = [i + 1 for i in range(m)]
        for q in queries:
            idx = p.index(q)
            retIndexlist.append(idx)
            p.pop(idx)
            p.insert(0, q)
        return retIndexlist
