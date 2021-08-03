class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = []
        res = []
        for x in range(m):
            p.append(x + 1)
        for x in queries:
            idx = p.index(x)
            res.append(idx)
            p.insert(0, p.pop(idx))

        return res
