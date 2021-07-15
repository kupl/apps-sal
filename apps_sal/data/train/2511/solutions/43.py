class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        a = set()
        for i in A:
            if i in a:
                return i
            else:
                a.add(i)
