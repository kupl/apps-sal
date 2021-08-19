class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            len1 = A[i]
            len2 = A[i - 1]
            len3 = A[i - 2]
            if self.check_triangle(len1, len2, len3):
                return len1 + len2 + len3
        return 0

    def check_triangle(self, len1, len2, len3):
        if len1 + len2 <= len3 or len2 + len3 <= len1 or len1 + len3 <= len2:
            return False
        return True
