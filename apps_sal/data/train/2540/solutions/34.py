class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        n = len(A)
        A.sort(reverse=True)
        a = 0
        while a < n:
            b = a + 1
            c = a + 2
            while b < n and c < n:
                if A[b] + A[c] > A[a]:
                    return A[a] + A[b] + A[c]
                else:
                    b += 1
                    c += 1
            a += 1
        return 0
