class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = []
        for i in range(1, m + 1):
            p.append(i)
        l = []

        for i in range(0, len(queries)):
            for j in range(0, m):
                if p[j] == queries[i]:
                    k = p.pop(j)
                    p.insert(0, k)
                    l.append(j)
                    break
        return l
