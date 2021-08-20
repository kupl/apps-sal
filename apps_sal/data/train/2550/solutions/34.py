class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        amount = [0 for i in range(2)]
        for bill in bills:
            if bill == 5:
                amount[0] += 1
            elif bill == 10:
                if amount[0] == 0:
                    return False
                else:
                    amount[1] += 1
                    amount[0] -= 1
            elif bill == 20:
                if amount[1] > 0 and amount[0] > 0:
                    amount[1] -= 1
                    amount[0] -= 1
                elif amount[0] > 2:
                    amount[0] -= 3
                else:
                    return False
        return True
