class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorarr = [0]
        for n in arr:
            xorarr.append(xorarr[-1] ^ n)

        res = []
        for i, j in queries:
            res.append(xorarr[j + 1] ^ xorarr[i])

        return res
