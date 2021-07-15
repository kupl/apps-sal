class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        B_dt = collections.Counter(B[0])
        for b in B[1:]:
            B_dt = B_dt | collections.Counter(b)
        ans = []
        
        for a in A:
            if collections.Counter(a) & B_dt == B_dt:
                ans.append(a)
    
        return ans
            
        

