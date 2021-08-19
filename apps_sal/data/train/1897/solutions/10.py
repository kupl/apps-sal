class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if len(arr) == 1:
            return [arr[0] for i in queries]
        table = [arr[0]] * len(arr)
        for i in range(1, len(arr)):
            table[i] = table[i - 1] ^ arr[i]
        '\n        print(table)\n        print(arr[0])\n        print(arr[0]^arr[1])\n        print(arr[0]^arr[1]^arr[2])\n        print(arr[0]^arr[1]^arr[2]^arr[3\n        '
        '\n        table = [out]*len(arr)\n        for i in range(1,len(arr)):\n            for j in range(i,len(arr)):\n                table[i][j] = table[i-1][j] ^ arr[j]\n        '
        out = [0] * len(queries)
        for (i, (l, r)) in enumerate(queries):
            if l > 0:
                out[i] = table[l - 1] ^ table[r]
            else:
                out[i] = table[r]
        return out
