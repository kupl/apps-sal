class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # precompute xor values
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        for i, q in enumerate(queries):
            if q[0] == 0:
                queries[i] = arr[q[1]]
            else:
                queries[i] = arr[q[0] - 1] ^ arr[q[1]]
        return queries
