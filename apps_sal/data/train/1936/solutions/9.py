import numpy as np
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        def findCounterpart(num: int) -> int:
            pow_flr = int(np.floor(np.log2(num)))
            layer = list(range(2 ** pow_flr, 2 ** (pow_flr + 1)))
            return layer[-layer.index(num)-1]
        res = [label]
        now = label
        while now != 1:
            now = findCounterpart(now // 2)
            res.insert(0, now)
        return res
