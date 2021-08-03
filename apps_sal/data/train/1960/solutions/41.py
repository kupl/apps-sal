class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m + 1)]
        res = []
        for q in queries:
            for i in range(len(p)):
                if p[i] == q:
                    res.append(i)
                    p.remove(q)
                    p.insert(0, q)
        return res
