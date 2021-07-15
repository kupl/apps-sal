class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) <= 2:
            return arr[0]
        lim = len(arr) // 4
        count = 1
        for num1, num2 in zip(arr, arr[1:]):
            if num1 == num2:
                count += 1
                if count > lim:
                    return num1
            else:
                count = 1
