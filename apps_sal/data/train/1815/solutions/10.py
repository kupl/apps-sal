class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        n = len(shifts)
        A = [0] * n
        
        def shifting(ch, k):
            return chr(((ord(ch) - 97 + k) % 26) + 97)
        
        A[-1] = shifts[-1]
        
        for i in range(n-2, -1, -1):
            A[i] = A[i+1] + shifts[i]
            
        return ''.join([shifting(c, A[i]) for i, c in enumerate(list(S))])
            
        
            
        

