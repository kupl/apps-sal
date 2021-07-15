class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        A_counter = [Counter(a) for a in A]
        B_counter = [Counter(b) for b in B]
        b_merged = Counter()
        for chr_ in string.ascii_lowercase:
            b_merged[chr_] = max([bc[chr_] for bc in B_counter])
        
        def is_subset(ac, bc):
            for chr_ in string.ascii_lowercase:
                if ac[chr_] < bc[chr_]:
                    return False
            return True
        
        ans = []
        for i,ac in enumerate(A_counter):
            if is_subset(ac,b_merged):
                ans.append(A[i])
        
        return ans
