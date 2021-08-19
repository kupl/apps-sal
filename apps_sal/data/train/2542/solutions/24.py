class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        #         inc = all([A[i]<=A[i+1] for i in range(0,len(A)-1)])
        #         dec = all([A[i]>=A[i+1] for i in range(0,len(A)-1)])

        #         return inc or dec

        #         inc = True
        #         dec = True

        #         for i in range(0,len(A)-1):
        #             if A[i]>A[i+1]:
        #                 inc=False
        #             if A[i]<A[i+1]:
        #                 dec=False

        #             if not inc and not dec:
        #                 return False

        #         return inc or dec

        #         if A[-1] > A[0]:
        #             return all(A[i] <= A[i + 1] for i in range(0, len(A) - 1))

        #         else:
        #             return all(A[i] >= A[i + 1] for i in range(0, len(A) - 1))

        if A[-1] > A[0]:
            inc = True
            for i in range(0, len(A) - 1):
                if A[i] > A[i + 1]:
                    return False
            else:
                return True

        else:
            dec = True
            for i in range(0, len(A) - 1):
                if A[i] < A[i + 1]:
                    return False
            else:
                return True
