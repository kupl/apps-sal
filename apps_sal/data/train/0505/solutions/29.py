class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        open_q = list()
        drop = list()
        
        for idx in range(len(s)):
            if s[idx] not in ['(', ')']:
                continue
                
            if s[idx] == '(':
                open_q.append(idx)
            
            else:
                
                if open_q:
                    open_q.pop()
                
                else:
                    drop.append(idx)
                    
        if open_q:
            drop.extend(open_q)
        
        res = ''
        for idx in range(len(s)):
            if idx not in drop:
                res += s[idx]
        
        return res

