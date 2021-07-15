class Solution:
    


    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def helper(S):
            r = ''
            erase = 0
            for s in S[-1::-1]:
                if s == '#':
                    erase+=1
                elif s !='#' and erase == 0:
                    r=s+r
                elif s !='#' and erase >=1:
                    #r=s+r
                    erase-=1
                
                    
            return r
    
        return helper(S) == helper(T)
        
        

