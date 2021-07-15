class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        changes = 0
        is_increasing = False
        is_decreasing = False
        for i in range(0, n-1):
            if changes == 0:    
                if A[i] > A[i+1]:
                    changes += 1
                    is_decreasing = True
                elif A[i] == A[i+1]:
                    changes += 1
                else:
                    is_increasing = True
            elif changes == 1:
                if A[i] <= A[i+1]:
                    changes += 1
                else:
                    is_decreasing = True
            else:
                return False
        return changes < 2 and is_decreasing and is_increasing
                
                    
            

