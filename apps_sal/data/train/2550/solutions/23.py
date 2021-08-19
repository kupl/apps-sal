class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0
        count_10 = 0
        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                if count_5 < 1:
                    return False
                else:
                    count_5 -= 1
                    count_10 += 1
            elif count_10 >= 1 and count_5 >= 1:
                count_10 -= 1
                count_5 -= 1
            elif count_5 >= 3:
                count_5 -= 3
            else:
                return False
        return True
