class Solution:

    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        l = 0
        r = len(S) - 1
        while l < r:
            if not S[l].isalpha():
                l += 1
            if not S[r].isalpha():
                r -= 1
            if S[l].isalpha() and S[r].isalpha():
                (S[l], S[r]) = (S[r], S[l])
                l += 1
                r -= 1
        return ''.join(S)
