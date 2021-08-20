class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddFound = False
        numOdd = 0
        for num in arr:
            if num % 2 != 0:
                oddFound = True
                numOdd += 1
                if numOdd == 3:
                    return True
            else:
                oddFound = False
                numOdd = 0
        return False
