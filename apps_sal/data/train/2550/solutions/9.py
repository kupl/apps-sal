class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0, 20: 0}
        for a in bills:
            if a == 5:
                d[5] += 1
                continue
            if a == 10:
                d[10] += 1
                if d[5] == 0:
                    return False
                else:
                    d[5] -= 1
            else:
                d[20] += 1
                if not (d[10] and d[5]) and d[5] < 3:
                    return False
                if d[10]:
                    d[10] -= 1
                    d[5] -= 1
                else:
                    d[5] -= 3
        return True
