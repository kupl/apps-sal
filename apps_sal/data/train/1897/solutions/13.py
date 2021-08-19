class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = []
        xoraccum = 0
        for n in arr:
            xoraccum ^= n
            xors.append(xoraccum)
        ret = []
        for query in queries:
            (l, r) = (query[0], query[1])
            rxor = xors[r]
            lxor = 0 if l == 0 else xors[l - 1]
            ret.append(rxor ^ lxor)
        return ret
