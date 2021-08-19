class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        count = 0

        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                residual = A[i - 1] - A[i] + 1
                A[i] += residual
                count += residual

        return count

        # naive solution TLE O(n^2)
#         visited = set()
#         count = 0

#         for num in A:
#             if num in visited:
#                 while num in visited:
#                     num += 1
#                     count += 1
#             visited.add(num)

#         return count
