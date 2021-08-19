class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd1 = False
        odd2 = False
        for num in arr:
            if num % 2:
                if odd2:
                    return True
                odd2 = odd1
                odd1 = True
            else:
                odd1 = False
                odd2 = False
        return False
