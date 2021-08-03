class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        n = len(A)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if A[j] <= A[i] // 2:
                    break
                for k in range(j + 1, n):
                    if A[i] < A[j] + A[k]:
                        return A[i] + A[j] + A[k]
        return 0
