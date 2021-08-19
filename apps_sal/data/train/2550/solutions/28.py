class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        change_5 = 0
        change_10 = 0
        for b in bills:
            if b == 5:
                change_5 += 1
            if b == 10:
                if change_5 > 0:
                    change_5 -= 1
                    change_10 += 1
                else:
                    return False
            if b == 20:
                if change_10 > 0 and change_5 > 0:
                    change_5 -= 1
                    change_10 -= 1
                elif change_5 > 2:
                    change_5 -= 3
                else:
                    return False
        return True
