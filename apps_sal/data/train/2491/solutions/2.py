class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        cand = []
        for i in range(len(A)):
            if A[i] != B[i]:
                cand.append(i)
        if len(cand) > 2:
            return False
        if len(cand) == 1:
            return False
        if len(cand) == 2:
            i, j = cand
            if A[i] == B[j] and B[i] == A[j]:
                return True
            else:
                return False
        if len(cand) == 0:
            if len(set(list(A))) < len(A):
                return True
            else:
                return False
