class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arrLen = len(arr)
        maxCount = 0
        maxCountNumber = 0
        arrDict = {}
        for i in range(arrLen):
            if arr[i] not in arrDict:
                arrDict[arr[i]] = i
                numCount = arr.count(arr[i])
                if numCount > maxCount:
                    maxCountNumber = arr[i]
                    maxCount = numCount
        return maxCountNumber
