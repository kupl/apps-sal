class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_sum = [arr[0]]

        for i in range(1, len(arr)):
            prefix_sum.append(prefix_sum[-1] ^ arr[i])

        result = []

        for l, r in queries:
            result.append(prefix_sum[r])
            if l > 0:
                result[-1] ^= prefix_sum[l - 1]

        return result
