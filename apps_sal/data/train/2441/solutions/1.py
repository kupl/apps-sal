class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        while i<len(s)-1:
            if abs(ord(s[i])-ord(s[i+1]))==32:
                s=s[:i]+s[i+2:]
                i-=1
                i=max(0,i)
            else:
                i+=1
        return s
