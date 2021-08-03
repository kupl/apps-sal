class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        register = {}

        for bill in bills:
            if bill == 5:
                register[5] = register.get(5, 0) + 1
            elif bill == 10:
                if 5 in register and register[5] >= 1:
                    register[5] -= 1
                    register[10] = register.get(10, 0) + 1
                else:
                    return False
            elif bill == 20:
                if 5 in register and 10 in register and register[10] >= 1 and register[5] >= 1:
                    register[5] -= 1
                    register[10] -= 1
                    register[20] = register.get(20, 0) + 1
                elif 5 in register and register[5] >= 3:
                    register[5] -= 3
                    register[20] = register.get(20, 0) + 1
                else:
                    return False
        return True
