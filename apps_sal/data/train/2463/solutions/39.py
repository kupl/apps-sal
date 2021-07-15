class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        inflection = None
        if len(A) > 3:
            for i in range(0,len(A)- 1):
                if inflection is not None:
                    if A[i] < A[i+1]:
                        return False
                else:
                    if A[i] > A[i+1]:
                        inflection = i
            
            print(inflection,A[0:inflection],A[inflection:])
            
            if inflection is not None:
                if len(A[0:inflection]) and len(A[inflection:]):
                    if len(set(A[0:inflection]))+len(set(A[inflection:])) == len(A):
                        return True
                    else:
                        return False
                else:
                    return False
                    print(set(A[0:inflection]),len(A[0:inflection]),set(A[inflection:]),len(A[inflection:]))
                    return False
            else:
                return False
        elif len(A) == 3:
            if A[0] < A[1] and A[1] > A[2]:
                return True
            else:
                return False
        else:
            return False
