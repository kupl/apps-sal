class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m + 1)]
        res = []
        for query in queries:
            index = p.index(query)
            res.append(index)
            p.remove(query)
            p = [query] + p
        return res
