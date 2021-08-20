class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        prev = 0
        cur = 1
        while cur < len(A):
            if A[prev] <= A[cur]:
                prev += 1
                cur += 1
            else:
                break
        if cur >= len(A):
            return True
        prev = 0
        cur = 1
        while cur < len(A):
            if A[prev] >= A[cur]:
                prev += 1
                cur += 1
            else:
                break
        if cur >= len(A):
            return True
        return False
