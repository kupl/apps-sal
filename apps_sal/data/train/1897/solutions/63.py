class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        n = len(arr)
        tmp = [arr[0]]
        for i in range(1, n):
            tmp.append(tmp[-1] ^ arr[i])
        for x, y in queries:
            if x == 0:
                res.append(tmp[y])
            else:
                res.append(tmp[x - 1] ^ tmp[y])
        return res
