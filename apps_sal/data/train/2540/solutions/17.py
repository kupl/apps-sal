class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        first = 0
        second = 1
        mx = 0
        for third in range(2, len(A)):
            if A[first] + A[second] > A[third]:
                mx = max(mx, A[first] + A[second] + A[third])
            first += 1
            second += 1
        return mx
