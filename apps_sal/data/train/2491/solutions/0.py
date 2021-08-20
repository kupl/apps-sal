class Solution:

    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) < 2:
            return False
        if A == B:
            cnt = Counter(A)
            return bool([v for v in cnt.values() if v > 1])
        diffs = []
        for (i, a) in enumerate(A):
            if a != B[i]:
                diffs.append(i)
        if len(diffs) == 2:
            (i, j) = diffs
            return A[i] == B[j] and A[j] == B[i]
        return False
