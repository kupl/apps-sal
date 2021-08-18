class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if len(bills) == 0:
            return True
        numfive = 0
        numten = 0
        for payment in bills:
            if payment == 5:
                numfive += 1
            elif payment == 10:
                if numfive >= 1:
                    numfive -= 1
                    numten += 1
                else:
                    return False
            else:
                if numten >= 1 and numfive >= 1:
                    numten -= 1
                    numfive -= 1
                elif numfive >= 3:
                    numfive -= 3
                else:
                    return False
        return True
