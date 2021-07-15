class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if A == B and len(set(A)) < len(B): return True
        
        if len(A) != len(B): return False
        
        diff_A = []
        diff_B = []
        
        for i in range(len(A)):
            if A[i] != B[i]:
                diff_A.append(A[i])
                diff_B.append(B[i])
            
        return len(diff_A) == len(diff_B) == 2 and diff_A[::-1] == diff_B
