class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            newArr = arr[i:i + 3]
            if newArr[0] % 2 != 0 and newArr[1] % 2 != 0 and (newArr[2] % 2 != 0):
                return True
        return False
