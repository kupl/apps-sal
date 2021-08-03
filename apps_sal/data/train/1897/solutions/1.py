
'''
x ^ y = z

0 ^ 1 = 1
1 ^ 0 = 1
0 ^ 0 = 0
1 ^ 1 = 0

逆推：
z   y   x
1   1 = 0
1   0 = 1
0   0 = 0
0   1 = 1

可见，仍是异或。计算前缀即可
'''


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix_xor = [0] * n
        prefix_xor[0] = arr[0]
        for i in range(1, n):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i]
        ret = []
        for start, end in queries:
            if start == 0:
                ret.append(prefix_xor[end])
            else:
                ret.append(prefix_xor[start - 1] ^ prefix_xor[end])
        return ret
