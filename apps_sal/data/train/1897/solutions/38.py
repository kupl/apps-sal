class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xrr = [0 for i in range(len(arr))]
        xrr[0] = arr[0]
        for i in range(1, len(arr)):
            xrr[i] = xrr[i - 1] ^ arr[i]
        res = []
        for q in queries:
            l = q[0]
            r = q[1]
            if l == r:
                res.append(arr[l])
            elif l == 0:
                res.append(xrr[r])
            else:
                res.append(xrr[r] ^ xrr[l - 1])
        return res
