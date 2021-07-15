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
                if numten >= 1 and numfive >= 1: #GREEDY: if a customer pays with a 20 dollar bill, we want to provide the $15 change using as few bills as possible, i.e. we want to give them change using 1 10$ bill and 1 5$ bill instead of 3 5$ bills if possible. This is so we can have more 5$ bills on hand for later transactions (5$ bills are used as change for all transactions regardless of amount, whereas $10 bills should be saved as change for customers that pay $20)
                    numten -= 1
                    numfive -= 1
                elif numfive >= 3:
                    numfive -= 3
                else:
                    return False
        return True
                

