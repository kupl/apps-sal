class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        sa = [0] + arr[:]
        for i in range(1, len(sa)):
            sa[i] ^= sa[i - 1]
        ret = []
        for l, r in queries:
            ret.append(sa[r + 1] ^ sa[l])
        return ret
