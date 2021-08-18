class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        prefix = [None] * len(arr)
        res = [None] * len(queries)
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] ^ arr[i]
        for i in range(len(queries)):
            if queries[i][0] == 0:
                res[i] = prefix[queries[i][1]]
                continue
            res[i] = prefix[queries[i][1]] ^ prefix[queries[i][0] - 1]
        return res
