class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m + 1)]

        def find(p, q):
            for i in range(len(p)):
                if p[i] == q:
                    return i

        def update(p, i):
            return [p[i]] + p[:i] + p[i + 1:]
        res = []
        for i in range(len(queries)):
            q = find(p, queries[i])
            res.append(q)
            p = update(p, q)
        return res
