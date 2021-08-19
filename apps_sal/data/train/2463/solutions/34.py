class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        up = True
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                # flat
                return False
            if up:
                # going up
                if A[i] < A[i - 1]:
                    # going down
                    if i == 1:
                        # starting down is not valid
                        return False
                    up = False
            else:
                # going down
                if A[i] > A[i - 1]:
                    # going back up after down is not mountain
                    return False
        return not up
