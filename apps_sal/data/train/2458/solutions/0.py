class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lCount = rCount = 0
        retVal = 0

        for char in s:
            if char == 'R':
                rCount += 1
            else:
                lCount += 1

            if rCount == lCount:
                retVal += 1
                lCount = rCount = 0
        return retVal
