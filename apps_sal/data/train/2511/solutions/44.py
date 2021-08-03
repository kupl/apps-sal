class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        myDict = {}

        for i in A:

            myDict[i] = myDict.get(i, 0) + 1
            if myDict[i] == len(A) / 2:
                return i
