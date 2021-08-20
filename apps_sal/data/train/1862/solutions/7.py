class Solution:

    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        A = arr
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[x - 1:i:-1] + A[:i]
        return res
