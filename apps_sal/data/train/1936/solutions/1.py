import math


class Solution:

    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        level = math.ceil(math.log(label + 1, 2))
        res.append(label)
        if level % 2 == 1:
            label = label // 2
            level -= 1
            label = abs(pow(2, level) - label) + pow(2, level - 1) - 1
            res.append(label)

        while(label >= 1):
            if level % 2 == 1:
                level -= 1
                label = label // 2
                res.append(label)
            else:
                label = label // 2
                level -= 1
                res.append(abs(pow(2, level) - label) + pow(2, level - 1) - 1)
        res.pop()

        return res[::-1]
