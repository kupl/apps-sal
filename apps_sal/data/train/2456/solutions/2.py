class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1

        backS = backT = 0

        while True:
            while i >= 0 and (backS or S[i] == '
                backS += 1 if S[i] == '
                i -= 1
            while j >= 0 and (backT or T[j] == '
                backT += 1 if T[j] == '
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j=i - 1, j - 1
