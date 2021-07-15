class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        ans = []
        j = 0
        for i in range(len(A[0])):
            temp = []
            for k in range(len(A)):
                temp.append(A[k][j])
            ans.append(temp)
            j += 1
        count = 0
        for i in ans:
            temp = i[:]
            temp.sort()
            if temp != i:
                count += 1
        return count
