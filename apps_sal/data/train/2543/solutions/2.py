class Solution:

    def reverseOnlyLetters(self, S: str) -> str:
        if len(S) == 1:
            return S
        start = 0
        end = len(S) - 1
        S = list(S)
        while start < end:
            if S[start].isalpha():
                if S[end].isalpha():
                    (S[start], S[end]) = (S[end], S[start])
                    start += 1
                    end -= 1
                else:
                    end -= 1
            else:
                start += 1
        return ''.join(S)
