class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flow = None
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                if not flow:
                    flow = 'd'
                
                elif flow != 'd':
                    return False
                continue
            if  A[i] < A[i+1]:
                if not flow:
                    flow = 'i'
                elif flow != 'i':
                    return False
                continue
        return True
                        

