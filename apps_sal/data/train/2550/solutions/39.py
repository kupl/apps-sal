class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for coin in bills:
            if coin == 5:
                five += 1
            if coin == 10:
                ten += 1
                if five != 0:
                    five -= 1
                else:
                    return False
            if coin == 20:
                twenty += 1
                if five == 0:
                    return False
                elif five < 3 and ten == 0:
                    return False
                elif ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
        return True
