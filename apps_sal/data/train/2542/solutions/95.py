class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if (len(A) == 1):
            return 1
        
        dir = 0
        for (i,j) in zip(A, A[1:] + [A[len(A) - 1]]):
            if (i != j):   
                cdir = (i - j) / abs(i - j)           
                if (dir == 0):
                    dir = cdir
                elif (dir != cdir):
                    return 0

        return 1
                           

    
    

