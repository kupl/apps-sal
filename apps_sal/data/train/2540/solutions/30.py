class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        #要满足两个条件，一是三个相加最大，二是两边和大于第三边，先考虑满足条件一，看在条件一下条件二是否满足
        A = sorted(A,reverse=True)
        #A.sort(reverse = True)
        for i in range(len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
                

