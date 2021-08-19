class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor_arr = [0] * len(arr)
        xor_arr[0] = arr[0]
        for i in range(1, len(arr)):
            xor_arr[i] = xor_arr[i - 1] ^ arr[i]
        res = [0] * len(queries)
        for (i, (s, e)) in enumerate(queries):
            if s == e:
                res[i] = arr[s]
            elif s == 0:
                res[i] = xor_arr[e]
            else:
                res[i] = xor_arr[e] ^ xor_arr[s - 1]
        return res
