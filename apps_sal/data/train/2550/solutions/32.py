class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n5, n10 = 0, 0
        for i in bills:
            if i == 5:
                n5 += 1
            elif i == 10:
                n10 += 1
                n5 -= 1
            elif n10 > 0:
                n10 -= 1
                n5 -= 1
            else:
                n5 -= 3
            if n5 < 0:
                return False
        return True
