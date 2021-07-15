class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        cnt_left = 0
        rev_left = []
        rev_right = set()
        
        for i, c in enumerate(s):
            if c == ')':
                if cnt_left == 0:
                    rev_right.add(i)
                else:
                    rev_left.pop()
                    cnt_left -= 1
            elif c =='(':
                rev_left.append(i)
                cnt_left += 1
        rev = rev_right.union(set(rev_left))
        
        res = []
        for i in range(len(s)):
            if i not in rev_right and i not in rev_left:
                res.append(s[i])
        return ''.join(res) 
                
                
            
        
        

