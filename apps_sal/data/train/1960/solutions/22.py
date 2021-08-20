class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []
        arr = [i for i in range(1, m + 1)]
        for q in queries:
            idx = arr.index(q)
            res.append(idx)
            arr.insert(0, arr.pop(idx))
        return res
