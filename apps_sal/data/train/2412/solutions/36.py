def remove_dupes(s):
    i = 0
    out = []
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            i += 2
        else:
            out.append(s[i])
            i += 1
    return ''.join(out)
        
    
class Solution:
    def removeDuplicates(self, s: str) -> str:
        prev = None
        while s != prev:
            s, prev = remove_dupes(s), s
        return s
            

