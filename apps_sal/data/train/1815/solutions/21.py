class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
#         def do(s, x):
#             return chr((ord(s)-ord('a')+x)%26+ord('a'))
        
#         S = list(S)
#         for i, x in enumerate(shifts):
#             for j, c in enumerate(S[:i+1]):
#                 S[j] = do(c, x)
#         return \"\".join(S)
        
        def do(s, x):
            return chr((ord(s)-ord('a')+x)%26+ord('a'))

        pre = []
        for s in shifts[::-1]:
            if(not pre):
                pre.append(s)
            else:
                pre.append(pre[-1]+s)
        
        S = list(S)
        for i in range(len(S)):
            S[i] = do(S[i], pre.pop())
        return \"\".join(S)
