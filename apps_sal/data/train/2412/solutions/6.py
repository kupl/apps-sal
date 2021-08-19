class Solution:

    def removeDuplicates(self, S: str) -> str:
        i = 0
        while i < len(S) - 1:
            if S[i] != S[i + 1]:
                i += 1
                continue
            else:
                S = S[0:i] + S[i + 2:]
                if i > 0:
                    i -= 1
        return S
