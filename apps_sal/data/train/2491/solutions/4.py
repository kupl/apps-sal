class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        if A == B and len(set(A)) < len(A):
            return True
        
        diffs = [(a, b) for a, b in zip(A, B) if a!= b]
        
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
