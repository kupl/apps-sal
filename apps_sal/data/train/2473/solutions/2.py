class Solution:
    def modifyString(self, s: str) -> str:
        r = ''
        
        if s[0] == '?':
            r += 'b' if (len(s) > 1 and s[1] == 'a') else 'a'
        else:
            r += s[0]
        
        for i in range(1, len(s) - 1):
            if s[i] == '?':
                if r[i - 1] != 'a' and s[i + 1] != 'a':
                    r += 'a'
                elif r[i - 1] != 'b' and s[i + 1] != 'b':
                    r += 'b'
                else:
                    r += 'c'
            else:
                r += s[i]
                    
        if len(s) > 1:
            if s[len(s) - 1] == '?':
                r += 'b' if r[len(s) - 2] == 'a' else 'a'
            else:
                r += s[len(s) - 1]
            
        return r
            

