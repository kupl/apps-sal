class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0
        maxCount = 0
        maxInt = arr[0]
        currInt = arr[0]
        for x in arr:
            if x != currInt:
                if count > maxCount:
                    maxCount = count
                    maxInt = currInt
                currInt = x
                count = 1
            else:
                count += 1
        if count > maxCount:
            maxCount = count
            maxInt = currInt
        return maxInt
