class Solution:
    def lemonadeChange(self, arr: List[int]) -> bool:
        five = 0
        ten = 0
        twen = 0
        for i in arr:
            if i == 5:
                five += 1
            elif i == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                s = min(five, ten)
                if s > 0:
                    five -= 1
                    ten -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True
