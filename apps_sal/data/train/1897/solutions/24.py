class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xored = [None] * len(arr)
        ans = [None] * len(queries)

        # construct the array xored = [arr[0],                arr[0]^arr[1],...,arr[0]^arr[1]^...^arr[i]^...^arr[n] ] of comulative xored elements of arr
        xored[0] = arr[0]
        for i in range(1, len(arr)):
            xored[i] = xored[i - 1] ^ arr[i]

        # now, because of the XOR property of x^x=0 and its distributive natur we get xored[L-1]^xored[R] = arr[0]^...^.arr[L-1]^arr[0]^...^arr[R]=arr[L]^...^arr[R] as required
        # (unless L==0 then the answer is simply xored[R])
        for i in range(len(queries)):
            L = queries[i][0]
            R = queries[i][1]
            if L > 0:
                ans[i] = xored[L - 1] ^ xored[R]
            else:
                ans[i] = xored[R]
        return ans
