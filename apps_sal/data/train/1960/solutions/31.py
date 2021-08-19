class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        if m == 1:
            return [0 for _ in range(len(queries))]
        p = [i + 1 for i in range(m)]
        res = []
        for i in queries:
            prev = p[0]
            if prev == i:
                res.append(0)
            else:
                j = 1
                while j < m:
                    tmp = p[j]
                    p[j] = prev
                    if tmp == i:
                        p[0] = tmp
                        res.append(j)
                        break
                    prev = tmp
                    j += 1
        return res
