class Solution:
    
    def __init__(self):
        self.f = True
    
    def impl(self, arr, i, incr):
        self.f = incr
        if (i + 1 >= len(arr)):
            return True

        if (arr[i + 1] > arr[i] and not incr):
            return False

        elif (arr[i + 1] < arr[i] and incr):
            incr = False

        elif(arr[i + 1] == arr[i]):
            return False

        return self.impl(arr, i + 1, incr)

    def validMountainArray(self, A) -> bool:
        if (A == None or len(A) <= 2):
            return False
        if(A[1]<A[0]):
            return False
        self.f = True
        result  = self.impl(A, 0, True)
        if(self.f):
            return False
        return result
        
        
        

