class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            bank[bill] += 1
            change = bill - 5
            if change and (not bank[5]):
                return False
            elif change == 15:
                if bank[10]:
                    bank[10] -= 1
                    bank[5] -= 1
                elif bank[5] >= 3:
                    bank[5] -= 3
                else:
                    return False
            elif change == 5:
                if bank[5]:
                    bank[5] -= 1
                else:
                    return False
        return True
