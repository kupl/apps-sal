class Solution:
    def modifyString(self, s: str) -> str:
        chars = list(map(chr, list(range(97, 123))))
        s = list(s)
        for i in range(0, len(s)):
            for x in chars:
                if(s[i] == '?'):
                    if(i == len(s) - 1):
                        if(s[i - 1] != x):
                            s[i] = x
                    elif(s[i - 1] != x and s[i + 1] != x):
                        s[i] = x
        return ''.join(s)
