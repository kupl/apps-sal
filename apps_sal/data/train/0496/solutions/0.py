class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        
        A.sort()
        prev = A[0]
        res = 0
        for num in A[1:]:
            if num <= prev:
                prev += 1
                res += prev-num

            else:
                prev = num
        
        return res

