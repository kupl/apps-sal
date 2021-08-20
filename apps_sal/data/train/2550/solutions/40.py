class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        _5 = 0
        _10 = 0
        for eachBill in bills:
            if eachBill == 5:
                _5 += 1
            elif eachBill == 10:
                if _5 >= 1:
                    _5 -= 1
                else:
                    return False
                _10 += 1
            elif eachBill == 20:
                if _10 >= 1 and _5 >= 1:
                    _10 -= 1
                    _5 -= 1
                elif _5 >= 3:
                    _5 -= 3
                else:
                    return False
            print(_5, _10, eachBill)
        return True
