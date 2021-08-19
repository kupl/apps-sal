class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        c = collections.Counter(A)
        for k in c:
            if c[k] == len(A) // 2:
                break
        return k
