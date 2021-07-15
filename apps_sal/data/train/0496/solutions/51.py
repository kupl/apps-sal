class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        i = 1
        stack = []
        current = A[0]
        moves = 0
        while i < len(A):
            if A[i] == A[i-1]:
                stack.append(A[i])
            elif len(stack) > 0:
                for num in range(current + 1, A[i]):
                    moves += num - stack.pop()
                    if not stack:
                        break
            current = A[i]
            i += 1
        
        while stack:
            moves += current + 1 - stack.pop()
            current += 1
        return moves
                

