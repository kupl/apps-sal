class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:

        n5 = 0
        n10 = 0
        for i in bills:
            if i == 5:
                n5 += 1
            elif i == 10:
                if n5 <= 0:
                    return False
                else:
                    n5 -= 1
                    n10 += 1
            else:
                if n10 > 0 and n5 > 0:
                    n10 -= 1
                    n5 -= 1
                elif n5 >= 3:
                    n5 -= 3
                else:
                    return False
        else:
            return True
