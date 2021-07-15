class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1,m+1)]
        res =[]
        for i in range(len(queries)):
            for j in range(m):
                if p[j] == queries[i]:
                    res.append(j)
                    p = [p[j]] + p[0:j]+p[j+1:]
        return res
