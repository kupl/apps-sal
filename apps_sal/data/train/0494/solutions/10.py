class Solution:
    def longestDecomposition(self, text: str) -> int:
        
        @lru_cache(None)
        def helper(i,j):
            if(i>j):
                return 0
            if(i == j):
                return 1

            ans = 1
            tmp = 0
            l = j-i+1
            for k in range(1,(l//2)+1):
                if(text[i:i+k] == text[j-k+1:j+1]):
                    #print(i,j,k,text[i:i+k],text[j-k+1:j+1])
                    tmp = max(tmp, 2+ helper(i+k,j-k))
            return max(tmp,1)
    
        return helper(0,len(text)-1)
                
                

