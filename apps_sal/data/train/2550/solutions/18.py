class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for b in bills:
            if b == 5:
                five += 1
            if b == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            if b == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif ten == 0 and five >= 3:
                    five -= 3
                else:
                    return False
        return True
