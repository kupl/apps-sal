class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        l = list(range(1,m+1))
        n = 0
        p = [0]*len(queries)
        for k in range(len(queries)):
            for i in range(len(l)):
                if l[i] == queries[k]:
                    l.insert(0,l.pop(i))
                    p[n] = i
                    n += 1
        return p
