class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if (arr.count(arr[i]) / len(arr)) > 0.25:
                s = arr[i]
                break
        return s
