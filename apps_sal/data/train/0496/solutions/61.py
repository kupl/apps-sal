class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        B=[A[0]]
        move=0
        for a in A[1:]:
            if a<=B[-1]:
                step=B[-1]-a+1
                move+=step
                a=a+step
            B.append(a)
                
        return move

