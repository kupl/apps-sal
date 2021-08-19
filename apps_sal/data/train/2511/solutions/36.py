class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        myDict = collections.Counter(A)
        for _ in myDict:
            if myDict[_] > 1:
                return _
