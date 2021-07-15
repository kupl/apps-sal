class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        cnt_left = 0
        rev_left, rev_right = [], []
        
        for i, c in enumerate(s):
            if c == ')':
                if cnt_left == 0:
                    rev_right.append(i)
                else:
                    rev_left.pop()
                    cnt_left -= 1
            elif c =='(':
                rev_left.append(i)
                cnt_left += 1
        res = ''
        for i in range(len(s)):
            if i not in rev_right and i not in rev_left:
                res += s[i]
        return res 
                
            
        
        

