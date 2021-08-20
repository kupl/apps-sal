class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return False
        else:
            if A[1] < A[0]:
                return False
            is_up = True
            curr = A[0]
            for n in A[1:]:
                if n == curr:
                    return False
                if n < curr:
                    is_up = False
                    curr = n
                if n > curr:
                    if is_up:
                        curr = n
                    else:
                        return False
            return not is_up
