class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        elif arr[0] % 2 + arr[1] % 2 + arr[2] % 2 == 3:
            return True
        else:
            return self.threeConsecutiveOdds(arr[1:])
