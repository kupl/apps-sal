class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        for i in range(len(A)):
            if A[i] == B[0]:
                divisible = True if (len(B) - (len(A) - i)) % len(A) == 0 else False
                time = 1 + (len(B) - (len(A) - i)) // len(A) if divisible else 1 + (len(B) - (len(A) - i)) // len(A) + 1
                repeatA = A * time
                if repeatA[i:i + len(B)] == B:
                    return time
        return -1
