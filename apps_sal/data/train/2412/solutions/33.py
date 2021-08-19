class Solution:

    def removeDuplicates(self, S: str) -> str:
        if len(S) <= 1:
            return S
        duplicateFound = True
        output = []
        while duplicateFound:
            duplicateFound = False
            i = 0
            while i < len(S):
                if i < len(S) - 1 and S[i] == S[i + 1]:
                    duplicateFound = True
                    i += 2
                    continue
                output.append(S[i])
                i += 1
            S = output
            output = []
        return ''.join(S)
