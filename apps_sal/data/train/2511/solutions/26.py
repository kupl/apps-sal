class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        sA = sorted(A)
        temp = None
        for i in sA:
            if i == temp:
                return i
            temp = i
