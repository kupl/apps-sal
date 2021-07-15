from collections import defaultdict, Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        rd = defaultdict(int)
        for c in map(Counter, B):
            for i in c:
                rd[i] = max(rd[i], c[i])
        
        # b = \"\".join([i * rd[i] for i in rd])
        
        cts = {i : Counter(i) for i in A}
        for i in rd:        
            rdi = rd[i]
            keep = {}
            for c in cts:
                if i in cts[c] and cts[c][i] >= rdi:
                    keep[c] = cts[c] 
            cts = keep        
        return cts        
                    
        
                
                
            
                

