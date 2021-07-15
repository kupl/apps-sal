class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        while(i != len(S)-1 and len(S) > 1):
            if(S[i] == S[i+1]):
                S = S[:i] + S[i+2:]
                i = 0 if(not i) else i-1
            else:
                i += 1
        return S
                
            

