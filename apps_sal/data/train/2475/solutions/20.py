class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        c_l = len(A[0])
        A_l = len(A)
        count = 0
        for i in range(c_l):
            string = [col[i] for col in A]
            for j in range(1, A_l):
                if string[j] < string[j - 1]:
                    count += 1
                    break
        return count
