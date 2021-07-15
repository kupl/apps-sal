class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a={}
        j=0
        s=list(s)
        i=0
        while i<len(s):
            if not s[i].isalpha():
                a[i+j]=s[i]
                del s[i]
                j+=1
            else:
                i+=1
        s=s[::-1]
        for i in a:
            s.insert(i,a[i])
        return ''.join(s)
