class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        if not A or len(A) < 3:
            return False
        (l, r) = (0, len(A) - 1)
        while l < r:
            if A[l] < A[l + 1] and A[r - 1] > A[r]:
                l += 1
                r -= 1
            elif A[l] < A[l + 1]:
                l += 1
            elif A[r - 1] > A[r]:
                r -= 1
            else:
                return False
            print(l, r)
        if l == r and l != 0 and (r != len(A) - 1):
            return True
        else:
            return False
