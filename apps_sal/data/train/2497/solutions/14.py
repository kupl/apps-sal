class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                odds += 1
            else:
                odds = 0
            if odds >= 3:
                return True
        return False
