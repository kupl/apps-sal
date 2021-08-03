class Solution:
    def shiftingLetters(self, S: str, shift: List[int]) -> str:
        j = 1
        S = list(S)
        resTot = []
        for i in reversed(shift):
            if resTot:
                resTot = [resTot[0] + i] + resTot
            else:
                resTot = [i]
        #print(resTot)
        for i in range(len(resTot)):
            asci_val = ord(S[i]) + (resTot[i] % 26) - ord('a')
            S[i] = chr((asci_val % 26) + ord('a'))
        
        # for i in shifts:
        #     for k in range(j):
        #         asci_val = (ord(S[k]) + i - ord('a')) % 26
        #         S[k] = chr(asci_val + ord('a'))
        #     j += 1
        return \"\".join(S)
