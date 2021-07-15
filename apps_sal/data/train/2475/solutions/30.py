class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        # check ascending order = comparison O(1)
        
        do_not_remove_idx = []
        for idx in range(len(A[0])):
            tmp = [a[idx] for a in A]
                    
            if any(x > y for x, y in zip(tmp, tmp[1:])):
                do_not_remove_idx.append(idx)
        
        return len(do_not_remove_idx)
