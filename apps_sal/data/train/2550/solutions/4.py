class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill = [0] * 3

        for b in bills:
            if b == 20:
                bill[2] += 1
                if bill[1] > 0:
                    bill[1] -= 1
                    bill[0] -= 1
                else:
                    bill[0] -= 3
            elif b == 10:
                bill[1] += 1
                bill[0] -= 1
            else:
                bill[0] += 1

            if sum(1 for i in bill if i < 0) > 0:
                return False

        return True
