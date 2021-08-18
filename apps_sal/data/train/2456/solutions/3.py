class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1

        skip_S = 0
        skip_T = 0

        while i >= 0 or j >= 0:
            while i >= 0 and (S[i] == '
                if S[i] == '
                    skip_S += 1
                else:
                    skip_S -= 1
                i -= 1

            while j >= 0 and (T[j] == '
                if T[j] == '
                    skip_T += 1
                else:
                    skip_T -= 1
                j -= 1

            if i < 0 and j < 0:
                return True
            elif i >= 0 and j >= 0:
                if S[i] == T[j]:
                    i -= 1
                    j -= 1
                else:
                    return False
            elif i >= 0 or j >= 0:
                return False
        return True
