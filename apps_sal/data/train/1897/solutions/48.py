class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        out = []
        tree = [0] * (2 * n)
        for i in range(n):
            tree[i + n] = arr[i]
        for i in range(n - 1, 0, -1):
            tree[i] = tree[i << 1] ^ tree[i << 1 | 1]
        for q in queries:
            res = 0
            l = q[0] + n
            r = q[1] + n + 1
            while l < r:
                if l & 1:
                    res = res ^ tree[l]
                    l = l + 1
                if r & 1:
                    r = r - 1
                    res = res ^ tree[r]
                l >>= 1
                r >>= 1
            out.append(res)
        return out
