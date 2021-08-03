class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        count = 0
        count2 = 0
        for x in range(len(A) - 1):
            if(A[x] <= A[x + 1]):
                count += 1
            if(A[x] >= A[x + 1]):
                count2 += 1
                print(count2, A[x])

        if(count == len(A) - 1 or count2 == len(A) - 1):
            return True
        else:
            return False
