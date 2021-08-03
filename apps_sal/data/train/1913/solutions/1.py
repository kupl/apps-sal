class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                break
        else:
            return A
        stack = []
        for j in range(i + 1, len(A)):
            if A[j] < A[i]:
                while stack and A[stack[-1]] < A[j]:
                    stack.pop()
                stack.append(j)
        A[i], A[stack[0]] = A[stack[0]], A[i]
        return A
