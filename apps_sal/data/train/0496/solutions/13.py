class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        A.sort()
        stack = []
        ans = 0
        A.append(A[-1] + n)
        for i in range(1, n + 1):
            if A[i] == A[i - 1]:
                stack.append(A[i])
            else:
                for r in range(1, A[i] - A[i - 1]):
                    if stack:
                        ans += A[i - 1] + r - stack.pop()
                    else:
                        break
        return ans
