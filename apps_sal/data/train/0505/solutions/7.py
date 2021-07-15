class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        c, st, st2,  res = 0, [], [], []
        for j, ss in enumerate(s):
            if ss == '(':
                st.append(j)
            elif ss == ')':
                if st:
                    st.pop()
                else:
                    st2.append(j)
            else: continue
        
        print((st, st2))   
        for j, ss in enumerate(s):
            if (ss == '(' and j in st) or (ss == ')' and j in st2) : continue 
            res.append(ss)
                    
        return ''.join(res)
             

