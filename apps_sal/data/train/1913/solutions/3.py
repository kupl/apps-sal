class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                pm = None
                for j in range(n - 1, i, -1):
                    if A[j] >= A[i]:
                        continue
                    if pm is None:
                        pm = j
                    elif A[j] == A[pm]:
                        pm = j
                    else:
                        break
                A[i], A[pm] = A[pm], A[i]
                return A
        return A
