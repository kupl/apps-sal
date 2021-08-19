class Solution:
    def removeDuplicates(self, S: str) -> str:
        i, n = 0, len(S)
        for j in range(0, n):
            #S[i] = S[j]
            S = S[:i] + S[j] + S[i + 1:]
            if i > 0 and S[i - 1] == S[i]:
                i -= 2
            i += 1
        return S[:i]
