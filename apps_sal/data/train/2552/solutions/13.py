class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        temp = list(set(arr))
        for i in range(len(temp)):
            if arr.count(temp[i]) / len(arr) > 0.25:
                return temp[i]
