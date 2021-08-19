class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        l = []
        [1, 0, 3, 2]
        # ix=0
        # while ix<len(A)-1:
        #     if A[ix]>A[ix+1]:
        #         l.append(A[ix])
        #         ix+=2
        #         if A[ix]<l[-1]:return False
        #     else:
        #         ix+=1
        # return True
        if len(A) == 1:
            return True
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True
