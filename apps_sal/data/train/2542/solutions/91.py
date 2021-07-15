from enum import Enum
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return True
        
        class Comp(Enum):
            inc = 0
            eq = 1
            dec = 2
            
        def to_comp(left, right):
            if right > left:
                return Comp.inc
            elif right == left:
                return Comp.eq
            else:
                return Comp.dec
        
        comp = to_comp(A[0], A[1])
        
        for i in range(2, len(A)):
            new_comp = to_comp(A[i - 1], A[i])
            if new_comp == Comp.inc and comp == Comp.dec:
                return False
            elif new_comp == Comp.dec and comp == Comp.inc:
                return False
            if new_comp != Comp.eq:
                comp = new_comp
            
        return True
