class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xored = [None] * len(arr)
        ans = [None] * len(queries)
        xored[0] = arr[0]
        for i in range(1, len(arr)):
            xored[i] = xored[i - 1] ^ arr[i]
        for i in range(len(queries)):
            L = queries[i][0]
            R = queries[i][1]
            if L > 0:
                ans[i] = xored[L - 1] ^ xored[R]
            else:
                ans[i] = xored[R]
        return ans
