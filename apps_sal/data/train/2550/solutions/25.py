class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        table = dict.fromkeys([5, 10, 20], 0)
        for p in bills:
            table[p] = table.get(p) + 1
            key = p - 5
            if key != 0:
                if key == 5:
                    value = table.get(5)
                    if value > 0:
                        table[5] = value - 1
                    else:
                        return False
                elif key == 15:
                    value10 = table.get(10)
                    value5 = table.get(5)
                    if value10 > 0 and value5 > 0:
                        table[10] = value10 - 1
                        table[5] = value5 - 1
                    elif value5 > 3:
                        table[5] = value5 - 3
                    else:
                        return False
        return True
