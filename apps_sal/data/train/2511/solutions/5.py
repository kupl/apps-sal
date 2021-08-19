class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        rep = len(A) // 2
        d = {}
        for i in A:
            if i in d:
                d[i] += 1
            if i not in d:
                d[i] = 1
            if d[i] == rep:
                return i
