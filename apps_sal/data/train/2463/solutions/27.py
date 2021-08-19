class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        strict_inc = False
        strict_dec = False
        if len(A) > 2:
            for i in range(1, len(A)):
                if A[i] > A[i - 1]:
                    if strict_dec:
                        return False
                    strict_inc = True
                elif A[i] < A[i - 1]:
                    strict_dec = True
                else:
                    return False
            if strict_inc and strict_dec:
                return True
            else:
                return False
        else:
            return False
