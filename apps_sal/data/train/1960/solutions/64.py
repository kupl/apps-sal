class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m + 1)]
        res = []
        for j in range(len(queries)):
            idx = p.index(queries[j])
            fs = p[0:idx]
            ls = p[idx + 1:]
            p = [p[idx]] + fs + ls
            res.append(idx)
        return res
