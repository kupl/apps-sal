class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res3 = []
        
        a_idx = 0
        b_idx = 0
        
        if a_idx >= len(A) or b_idx >= len(B):
            return []
        
        redo_step = False

        while a_idx < len(A) and b_idx < len(B):
            next_a2 = A[a_idx]
            next_b2 = B[b_idx]
            i_a = next_a2[0]
            i_b = next_b2[0]
            
            if next_a2[1] < next_b2[1]:
                a_idx += 1
            else:
                b_idx += 1
                
                
            max_lft = max(k for k in [next_a2[0], next_b2[0]])
            min_rgt = min(k for k in [next_a2[1], next_b2[1]])

            if max_lft <= min_rgt:
                res3.append([max_lft, min_rgt])

        
        return res3
