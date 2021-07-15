class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st =[]
        remove = defaultdict(int)
        for ind,ch in enumerate(s):
            if ch is '(':
                st.append(ind)
            elif ch is ')':
                if st:
                    st.pop()
                else :
                    remove[ind]+=1
        print(remove)
        if st:
            dic = {elem:1 for elem in st}
            remove.update(dic)
            
        print(remove)
        
        ans = ''
        for ind,ch in enumerate(s):
             if remove[ind] == 0:
                    ans+=ch
                    
        return ans   
