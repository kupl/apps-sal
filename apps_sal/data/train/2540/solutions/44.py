class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for i in range(len(A) - 2):
            test = A[i:i + 3]
            if test[0] + test[1] > test[2] and test[2] - test[1] < test[0] and sum(test) > res:
                res = sum(test)
        return res
