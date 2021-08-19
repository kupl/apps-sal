class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        largeArr = {}
        tempCount = 0
        for num in arr:
            if num in largeArr:
                tempCount = tempCount + 1
                largeArr[num] = tempCount
            else:
                tempCount = 1
                largeArr[num] = tempCount
        max1 = max(largeArr.values())
        for key in list(largeArr.keys()):
            if largeArr[key] == max(largeArr.values()):
                return key
