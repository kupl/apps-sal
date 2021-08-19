class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(arr) - 1):
            arr[i + 1] ^= arr[i]
        res = []
        for (i, j) in queries:
            if i == 0:
                res.append(arr[j])
            else:
                res.append(arr[i - 1] ^ arr[j])
        return res
