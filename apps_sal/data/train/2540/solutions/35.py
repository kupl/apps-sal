class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if (len(A) < 3):
            return 0

        maxer = 0
        pointer1 = len(A) - 3
        pointer2 = len(A) - 2
        pointer3 = len(A) - 1
        A.sort()

        if len(A) == 3:
            if (A[0] + A[1] > A[2]):
                return sum(A)
            else:
                return 0

        while (pointer3 >= 2):
            if A[pointer1] + A[pointer2] > A[pointer3]:
                return A[pointer1] + A[pointer3] + A[pointer2]
            elif pointer1 == 0:
                pointer3 -= 1
                pointer2 = pointer3 - 1
                pointer1 = pointer2 - 1
            else:
                pointer1 -= 1
                pointer2 -= 1

        return maxer
