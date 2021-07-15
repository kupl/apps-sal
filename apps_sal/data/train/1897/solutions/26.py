class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        ret = []
        for l, r in queries:
            ret.append(arr[r] if l == 0 else arr[r] ^ arr[l - 1])
        return ret
