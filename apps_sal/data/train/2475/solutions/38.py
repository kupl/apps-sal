class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if len(A) == 0:
            return 0
        n = len(A[0])
        cnt = 0
        for i in range(n):
            is_sorted = True
            for j in range(len(A) - 1):
                if A[j][i] > A[j + 1][i]:
                    is_sorted = False
                    break
            if not is_sorted:
                cnt += 1
        return cnt
