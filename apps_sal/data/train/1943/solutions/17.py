class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        res3 = []
        
        def get_next_items(lft_idx, rgt_idx):
            lft_idx_outer = int(lft_idx / 2)
            lft_idx_inner = lft_idx % 2
            rgt_idx_outer = int(rgt_idx / 2)
            rgt_idx_inner = rgt_idx % 2
            lft = A[lft_idx_outer][lft_idx_inner] if lft_idx_outer < len(A) else None
            rgt = B[rgt_idx_outer][rgt_idx_inner] if rgt_idx_outer < len(B) else None
            lft_full = A[lft_idx_outer] if lft_idx_outer < len(A) else A[lft_idx_outer-1]
            rgt_full = B[rgt_idx_outer] if rgt_idx_outer < len(B) else B[rgt_idx_outer-1]
            return (lft, rgt, lft_full, rgt_full, min(lft_idx_outer, len(A)-1), min(rgt_idx_outer, len(B)-1))
        
        u = (0, 0)
        a_idx = 0
        b_idx = 0
        
        if a_idx >= len(A) or b_idx >= len(B):
            return []
        
        prev_counter_a = None
        prev_counter_b = None
        
        i_a, i_b, next_a2, next_b2, counter_a, counter_b = get_next_items(a_idx, b_idx)
        
        redo_step = True
        
        while not (i_a is None and i_b is None):
            if (i_a is not None and i_b is None) :
                a_idx += 1
            elif (i_a is None and i_b is not None):
                b_idx += 1
            elif (i_a < i_b):
                a_idx += 1
            elif (i_a > i_b):
                b_idx += 1
            elif (i_a == i_b) and redo_step:
                redo_step = False
            elif (i_a == i_b) and not redo_step:
                a_idx += 1
                b_idx += 1
                redo_step = True
                
            i = min(k for k in [i_a, i_b] if k is not None)

            if next_a2 is not None and next_b2 is not None and next_a2[0] <= i <= next_a2[1] and next_b2[0] <= i <= next_b2[1]:
                #intersections_append2((counter_a, counter_b), i)
                if counter_a == prev_counter_a and counter_b == prev_counter_b:
                    # append
                    res3[-1].append(i)
                else:
                    # add
                    res3.append([i])
                prev_counter_a = counter_a
                prev_counter_b = counter_b
                
            i_a, i_b, next_a2, next_b2, counter_a, counter_b = get_next_items(a_idx, b_idx)
        
        res4 = []
        for x in res3:
            if len(x) > 2:
                tmp = sorted(list(set(x)))
                res4.append(tmp)
            else:
                res4.append(x)
        
        return res4
