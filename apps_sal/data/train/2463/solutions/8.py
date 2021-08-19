class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        start = 0
        finish = len(A)
        print(len(A))
        for i in range(0, len(A) - 1):
            print(('i', i))
            if A[i] == A[i + 1]:
                return False
            elif A[i] > A[i + 1]:
                start = i
                print(('else1', start))
                break
        for j in range(0, len(A) - 1):
            print(('j', j))
            if A[len(A) - 1 - j] == A[len(A) - 2 - j]:
                return False
            elif A[len(A) - 1 - j] > A[len(A) - 2 - j]:
                print(('break2', len(A) - 1 - j, len(A) - 2 - j, A[len(A) - 1 - j], A[len(A) - 2 - j]))
                finish = len(A) - 1 - j
                break
        print(('s, f', start, finish))
        return start == finish and start > 0 and (finish < len(A))
