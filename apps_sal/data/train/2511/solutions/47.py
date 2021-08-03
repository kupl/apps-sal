class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # check the first elem first
        result = A[0]
        count = 0
        if A.count(result) == len(A) // 2:
            return result
        for i in A[1:]:
            if count == 0:
                result = i
                print('a')
                count = 1
            elif result == i:
                print('b')
                count += 1
            else:
                print('c')
                count -= 1

        return result
