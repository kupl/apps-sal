class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(arr) * 0.25:
                return num
