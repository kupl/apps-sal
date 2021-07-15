class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = []
        res = []
        for i in range(1, m + 1):
            p.append(i)
        for n in queries:
            pos = 0
            while p[pos] != n and pos < m:
                pos += 1
            res.append(pos)
            del p[pos]
            p.insert(0, n)
        return res
