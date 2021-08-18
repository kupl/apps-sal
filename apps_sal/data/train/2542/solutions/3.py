class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True

        direction = 0

        for i in range(len(A) - 1):
            j = i + 1
            tmp = A[i] - A[j]
            if tmp == 0:
                continue
            elif tmp > 0:
                if direction == 0 or direction == -1:
                    direction = -1
                else:
                    return False
            else:
                if direction == 0 or direction == 1:
                    direction = 1
                else:
                    return False

        return True
