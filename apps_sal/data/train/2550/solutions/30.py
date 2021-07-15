class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
            if bill == 10:
                if fives < 1:
                    return False
                tens += 1
                fives -= 1
            if bill == 20:
                if (tens < 1 and fives < 3) or (fives < 1):
                    return False
                elif (tens < 1):
                    fives -= 3
                else:
                    tens -= 1
                    fives -= 1
        
        return True
