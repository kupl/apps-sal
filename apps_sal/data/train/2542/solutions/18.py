class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        diff_lst = [A[i + 1] - A[i] for i in range(len(A) - 1)]
        positive = all((i >= 0 for i in diff_lst))
        negative = all((i <= 0 for i in diff_lst))
        return positive or negative
