class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        res = ''
        for x in range(1, len(A)):
            if A[x] > A[x - 1]:
                res = 'pos'
            elif A[x] == A[x - 1]:
                continue
            else:
                res = 'neg'
        if res != 'pos' and res != 'neg':
            return True
        for x in range(1, len(A)):
            if res == 'neg':
                if A[x] > A[x - 1]:
                    return False
                else:
                    continue
            elif A[x] < A[x - 1]:
                return False
            else:
                continue
        return True
