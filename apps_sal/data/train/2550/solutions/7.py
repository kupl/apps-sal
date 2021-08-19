class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            # now last two cases handle if it is a 20
            # if we have a ten give that and one five
            elif ten > 0:
                five -= 1
                ten -= 1
            # last option is to give 3 fives
            else:
                five -= 3
            # check if five is under zero then return false
            if five < 0:
                return False
        return True
