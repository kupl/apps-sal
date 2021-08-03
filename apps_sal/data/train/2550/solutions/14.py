class Solution:
    stack = {
        5: 0,
        10: 0,
        20: 0
    }

    def change(self, value: int):
        self.stack[value] += 1
        res = True

        if value == 10:
            if self.stack[5] > 0:
                self.stack[5] -= 1
            else:
                res = False

        if value == 20:
            if self.stack[10] > 0 and self.stack[5] > 0:
                self.stack[10] -= 1
                self.stack[5] -= 1
            elif self.stack[5] > 2:
                self.stack[5] -= 3
            else:
                res = False

#         print(self.stack)
        return res

    def lemonadeChange(self, bills: List[int]) -> bool:
        self.stack = {
            5: 0,
            10: 0,
            20: 0
        }

        res = False
        for b in bills:
            res = self.change(b)
            if not res:
                break
        return res
