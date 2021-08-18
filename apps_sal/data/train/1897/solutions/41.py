class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        for i, j in queries:
            if i == 0:
                res.append(arr[j])
            else:
                res.append(arr[i - 1] ^ arr[j])
        return res
