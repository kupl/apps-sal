class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        import numpy as np
        if len(A)==1:
            return(True)
        else:
            diff = np.diff(A)
            return(min(diff)>=0 or max(diff)<=0)

