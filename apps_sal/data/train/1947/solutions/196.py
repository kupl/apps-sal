class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        a_counter = [Counter(a) for a in A]
        b_counter = [Counter(b) for b in B]
        
        bc = {}
        for counter in b_counter:
            for b, frequency in counter.items():
                if b in bc:
                    bc[b] = max(bc[b], frequency)
                else:
                    bc[b] = frequency
                    
        def is_bc_in_ac(ai, ac):
            if len(bc) > len(A[ai]):
                return False

            for l, frequency in bc.items():
                if ac[l] < frequency:
                    return False
            return True
        
        res = []
        for ai, ac in enumerate(a_counter):
            if is_bc_in_ac(ai, ac):
                res.append(A[ai])
        return res
