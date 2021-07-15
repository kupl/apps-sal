class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length = len(A)
        if length < 3: return False
        
        prev = A[0]
        peak = -1
        
        for i in range (1, length):
            print(A[i])
            if A[i] > prev:
                if peak != -1:
                    return False
            elif A[i] == prev:
                return False
            else:
                if i == 1: 
                    return False
                peak = A[i]
            
            prev = A[i]
        
        print(peak)
        return True if peak != -1 else False
