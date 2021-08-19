class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return True
        last_diff = 0
        for i in range(1, len(A)):
            cur_diff = A[i] - A[i - 1]
            if cur_diff < 0:
                if last_diff == 0:
                    last_diff = cur_diff
                elif last_diff > 0:
                    return False
            elif cur_diff > 0:
                if last_diff == 0:
                    last_diff = cur_diff
                elif last_diff < 0:
                    return False
        return True
