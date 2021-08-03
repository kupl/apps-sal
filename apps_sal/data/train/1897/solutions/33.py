class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        a = arr
        q = queries
        l = []
        for i in range(len(a) - 1):
            a[i + 1] ^= a[i]
        print(a)
        for i, j in q:
            if i:
                l.append(a[j] ^ a[i - 1])
            else:
                l.append(a[j])
        return (l)
