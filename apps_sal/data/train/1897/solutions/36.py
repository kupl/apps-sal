class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(arr) - 1):
            arr[i+1] = arr[i+1] ^ arr[i]
        for i in queries:
            if i[0] == 0:
                res.append(arr[i[1]])
            else:
                res.append(arr[i[1]] ^ arr[i[0] - 1])
        return res
