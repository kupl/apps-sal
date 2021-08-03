class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:

        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                for j in range(i + 1, len(A)):
                    if A[j] > A[i] or j == len(A) - 1:
                        k = (j - 1) if A[j] > A[i] else j
                        while k > i and A[k] == A[i]:
                            k -= 1
                        while k - 1 > i and A[k - 1] == A[k]:
                            k -= 1
                        A[i], A[k] = A[k], A[i]
                        break
                break
        return A
