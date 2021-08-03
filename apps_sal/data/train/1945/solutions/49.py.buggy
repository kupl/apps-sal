class Solution:
    def maxEqualRowsAfterFlips(self, mat: List[List[int]]) -> int:
        
        
        s=collections.defaultdict(lambda: 0)
        m=len(mat)
        n=len(mat[0])
        st=\"\"
        maxi=0
        for i in range(m):
            for j in range(n-1):
                if(mat[i][j]==mat[i][j+1]):
                    st+='1'
                else: 
                    st+='0'
            s[st]+=1
            maxi=max(maxi, s[st])
            st=\"\"
        return maxi
        
        
    
