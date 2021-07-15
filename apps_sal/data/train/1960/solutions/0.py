class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        if not queries:
            return []
        p = list(range(1, m+1))
        res = []
        for i in queries:
            z = p.index(i)
            res.append(z)
            del p[z]
            p.insert(0,i)
        return res
            

