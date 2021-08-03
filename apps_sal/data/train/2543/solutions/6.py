class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        start = 0
        end = len(S) - 1
        while start <= end:
            while not S[start].isalpha() and start < end:
                start += 1
            while not S[end].isalpha() and start < end:
                end -= 1
            S[start], S[end] = S[end], S[start]
            start += 1
            end -= 1
        return ''.join(S)
