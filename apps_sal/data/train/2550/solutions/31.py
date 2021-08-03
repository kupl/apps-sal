class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        # n5=0
        # n10=0
        # for i in bills:
        #     if i == 5:
        #         n5 +=1
        #     elif i == 10:
        #         if n5<=0:
        #             return False
        #         else:
        #             n5 -=1
        #             n10 +=1
        #     else:
        #         if n10>0 and n5 >0:
        #             n10 -=1
        #             n5 -=1
        #         elif n5>=3:
        #             n5-=3
        #         else:
        #             return False
        # else:
        #     return True

        five = ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                five, ten = five - 1, ten + 1
            elif ten > 0:
                five, ten = five - 1, ten - 1
            else:
                five -= 3

            if five < 0:
                return False
        return True
