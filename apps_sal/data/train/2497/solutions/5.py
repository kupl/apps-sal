class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if self.is_odd(arr[i]) and self.is_odd(arr[i + 1]) and self.is_odd(arr[i + 2]):
                return True
        return False

    def is_odd(self, num):
        return num % 2 != 0
