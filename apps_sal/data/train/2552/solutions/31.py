class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        rate = len(arr) // 4

        count = [0 for i in range(100001)]

        for idx, value in enumerate(arr):
            count[value] += 1

            if count[value] > rate:
                return value

        return 0
