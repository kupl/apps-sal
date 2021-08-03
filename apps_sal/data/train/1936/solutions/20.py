class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = int(math.log2(label))
        res, count = [], 0
        while label > 0:
            res.append(label if count % 2 == 0 else (3 * 2 ** level - 1 - label))
            label >>= 1
            level -= 1
            count += 1

        return res[::-1]
