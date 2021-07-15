class Solution:
    def removeDuplicates(self, S: str) -> str:
        temp = len(S)-1
        temp1 = len(S)-1
        while True:
            temp1 = temp
            if len(S)>=2:
                i = 0
                while i<temp:
                    if S[i] == S[i+1]:
                        S = S[:i] + S[i+2:]
                        temp -= 2
                    i+=1
            if temp == temp1:
                return S
