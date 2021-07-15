class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d={}
        for i in A:
            if i in d:
                return i
            else:
                d[i]=1
