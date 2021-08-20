class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        if A[0] > A[1]:
            return False
        decreasing = False
        last = A.pop(0)
        while A:
            new = A.pop(0)
            print((new, last, decreasing))
            if new == last:
                return False
            if new > last and decreasing:
                print('early')
                return False
            if new < last and (not decreasing):
                decreasing = True
            last = new
        return decreasing
