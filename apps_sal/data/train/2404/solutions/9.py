class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        preNum = 0
        missNum = 0
        for currNum in arr:
            preMissNum = missNum
            missNum += currNum - preNum - 1
            if missNum >= k:
                res = preNum + k - preMissNum
                return res
            preNum = currNum

        res = preNum + k - missNum
        return res
