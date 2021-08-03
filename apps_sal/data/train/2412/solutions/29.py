class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        repeat = True
        while repeat:
            repeat = False
            new = ''
            while i < len(S):
                if i < len(S) - 1 and S[i] == S[i + 1]:
                    i += 2
                    repeat = True
                else:
                    new += S[i]
                    i += 1
            S = new
            i = 0
        return S
