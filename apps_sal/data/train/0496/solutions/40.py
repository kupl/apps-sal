class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # if len(A) < 2:
        #     return 0
        # index = []
        # count = 0
        # init = A[0]
        # for a in A:
        #     if a not in index:
        #         index.append(a)
        #     else:
        #         while a in index:
        #             count+=1
        #             a += 1
        #         index.append(a)
        # return count
        A.sort()
        ans = 0
        for i in range(1,len(A)):
            if A[i-1] >= A[i]:
                ans += A[i-1] - A[i] + 1
                A[i] += A[i-1] - A[i] + 1
                
        return ans
