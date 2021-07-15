class Solution:
    def xorQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(A) - 1):
            A[i + 1] ^= A[i]
    # prefix  xor
        return [A[j] ^ A[i - 1] if i else A[j] for i, j in queries] 
    # if i == 0  then a[j]

