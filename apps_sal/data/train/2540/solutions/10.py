class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # hold result.
        result = 0
        # sort the given lengths.
        A = sorted(A)
        # go through lengths, check for valid triangle.
        for i in range(len(A) - 2):
            # store triangle sides.
            a, b, c = A[i], A[i + 1], A[i + 2]
            # check if valid.
            if (a + b) > c and (a + c) > b and (b + c) > a:
                result = max(result, a + b + c)
        # return result.
        return result
