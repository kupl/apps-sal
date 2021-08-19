class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_xor = [0]
        size_arr = len(arr)
        if size_arr % 2 == 0:
            for i in range(0, size_arr, 2):
                pre_xor.append(pre_xor[i] ^ arr[i])
                pre_xor.append(pre_xor[i + 1] ^ arr[i + 1])
        else:
            pre_xor.append(pre_xor[0] ^ arr[0])
            for i in range(1, size_arr, 2):
                pre_xor.append(pre_xor[i] ^ arr[i])
                pre_xor.append(pre_xor[i + 1] ^ arr[i + 1])
        out_xor = []
        for (L, R) in queries:
            out_xor.append(pre_xor[L] ^ pre_xor[R + 1])
        return out_xor
