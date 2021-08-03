class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if A == B or B in A:
            return 1
        if A not in B:
            if B not in (A + A):
                return -1
            else:
                return 2
        else:
            count, i = 1, B.index(A)
            if i != 0:
                if B[:i] != A[-i:]:
                    return -1
                else:
                    count = 2
            while i + 2 * len(A) < len(B) and A == B[i + len(A):i + 2 * len(A)]:
                count += 1
                i = B.index(A, i + len(A))
            if i == len(B) - len(A):
                return count
            else:
                if B[i + len(A):] != A[:len(B) - i - len(A)]:
                    return -1
                return count + 1
