class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        \"\"\"
        res = -1
        for i in range(len(A)-1,0,-1):
        \"\"\"
        for i in range(len(A)-1,0,-1):
            if A[i] >= A[i-1]:
                continue
            else:
                val = A[i-1]
                j=-1
                while (A[j] >= val  or A[j] == A[j-1] ):
                    j-=1
            
            A[i-1], A[j] = A[j], A[i-1]
            break
        return A
