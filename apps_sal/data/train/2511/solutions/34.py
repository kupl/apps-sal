class Solution:
    def repeatedNTimes(self, A) -> int:
        B = list(A)
        B.sort()
        for i in range(0, len(B)):
            if B[i] == B[i + 1]:
                return B[i]
            else:
                pass


p = Solution()
testList = [5, 1, 5, 2, 5, 3, 5, 4]
print(p.repeatedNTimes(testList))
