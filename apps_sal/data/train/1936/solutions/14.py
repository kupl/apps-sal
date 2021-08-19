import math


class Solution:

    def pathInZigZagTree(self, label: int) -> List[int]:
        ret = [label]
        while label != 1:
            level = math.floor(math.log2(label))
            max_at_level = 2 ** (level + 1) - 1
            label = (max_at_level - label) // 2 + 2 ** (level - 1)
            ret.append(label)
        return reversed(ret)
