class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        tweens = 0
        for bill in bills:
            if bill > 10:
                tweens += 1
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives > 2:
                    fives -= 3
                else:
                    return False
            elif bill == 10:
                tens += 1
                if fives > 0:
                    fives -= 1
                else:
                    return False
            else:
                fives += 1
        return True
