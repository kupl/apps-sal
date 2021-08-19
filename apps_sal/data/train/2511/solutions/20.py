class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        size = len(A)
        n = size / 2
        appear = {}
        for i in range(size):
            if A[i] not in list(appear.keys()):
                appear[A[i]] = 1
            else:
                appear[A[i]] += 1
        for i in list(appear.items()):
            if i[1] == n:
                return i[0]
