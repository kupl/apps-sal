class Solution:
    
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def conv(w):
            sol = [0 for _ in range(26)]
            for c in w:
                sol[ord(c)-ord('a')] += 1
            return sol
        
        bmax = [0 for _ in range(26)]
        for wb in B:
            for idx, cnt in enumerate(conv(wb)):
                bmax[idx] = max(bmax[idx], cnt)
                
        sol = []
        for wa in A:
            if all(a>=b for a, b in zip(conv(wa), bmax)):
                sol.append(wa)
        return sol
            
            
            

