class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        size = len(A[0])
        setd = set([i for i in range(size)])
        for i in range(len(A) - 1) :
            if not setd :
                return size
            setn = set()
            for digit in setd:
                if A[i][digit] > A[i+1][digit] :
                    setn.add(digit)
            setd -= setn
         
        return size - len(setd)
