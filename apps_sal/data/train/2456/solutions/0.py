class Solution:
    def backspaceCompare(self, S1, S2):
        i1 = len(S1) - 1 
        i2 = len(S2) - 1
        
        while i1 >= 0 or i2 >= 0:
            c1 = ''
            c2 = ''
            if i1 >= 0:
                c1, i1 = self.getChar(S1, i1)
            if i2 >= 0:
                c2, i2 = self.getChar(S2, i2)
            if c1 != c2:
                return False
        return True
        
    
    def getChar(self, s, i):
        char = ''
        count = 0
        while i >= 0 and not char:
            if s[i] == '#':
                count += 1
            elif count == 0:
                char = s[i]
            else:
                count -= 1
            i -= 1
        return char, i


