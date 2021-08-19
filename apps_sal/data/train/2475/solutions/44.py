class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        N = len(A[0])
        count = 0
        for i in range(N):
            temp = []
            for j in range(len(A)):
                temp.append(A[j][i])
            if temp != sorted(temp):
                count += 1
        return count
