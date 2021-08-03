class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [arr[0]]

        n = len(arr)
        for i in range(1, n):
            xors.append(xors[-1] ^ arr[i])

        res = []
        for query in queries:
            l, r = query
            temp = xors[r]
            if l != 0:
                temp ^= xors[l - 1]
            res.append(temp)

        return res
