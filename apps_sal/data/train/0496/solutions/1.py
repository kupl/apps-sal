class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0

        n = len(A)
        A.sort()

        tail_num = A[0]
        result = 0
        for i in range(1, n):
            if A[i] > tail_num:
                tail_num = A[i]
            else:
                tail_num += 1

            # result = result + (tail_num - A[i])
            result += tail_num - A[i]

        return result
