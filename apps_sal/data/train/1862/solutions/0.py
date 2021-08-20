class Solution:

    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        res = []
        for x in range(n, 1, -1):
            idx = A.index(x)
            res.extend([idx + 1, x])
            A = A[idx::-1] + A[idx + 1:]
            A = A[x - 1::-1]
        return res
