class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_dict = {5: 0, 10: 0, 20: 0}
        for i in range(len(bills)):
            if bills[i] == 20:
                if bill_dict[10] == 0:
                    bill_dict[20] += 1
                    bill_dict[5] -= 3
                else:
                    bill_dict[20] += 1
                    bill_dict[10] -= 1
                    bill_dict[5] -= 1
            elif bills[i] == 10:
                bill_dict[10] += 1
                bill_dict[5] -= 1
            else:
                bill_dict[5] += 1
            if bill_dict[5] < 0 or bill_dict[10] < 0 or bill_dict[20] < 0:
                return False
        return True
