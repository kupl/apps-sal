class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        a = 0
        while a < len(arr) - 2:
            if arr[a] & 1 and arr[a + 1] & 1 and arr[a + 2] & 1:
                return True
            elif arr[a + 2] & 1 == 0:
                a += 3
            elif arr[a + 1] & 1 == 0:
                a += 2
            elif arr[a] & 1 == 0:
                a += 1
        return False
