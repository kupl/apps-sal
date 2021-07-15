class Solution:
    def removeDuplicates(self, S: str) -> str:
        found = True
        while(found):
            found = False
            for i in range(len(S)-1):
                if i >= len(S) - 1:
                    break
                elif S[i] == S[i+1]:
                    found = True
                    S = S[:i] + S[i+2:]
                    i -= 2
        return S
