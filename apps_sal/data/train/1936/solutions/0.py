class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        level = 0
        nodes_count = 0
        while nodes_count < label:
            nodes_count += 2**level
            level += 1
        while label != 0:
            res.append(label)
            level_max = (2**level) - 1
            level_min = 2**(level - 1)
            label = (level_max + level_min - label) // 2
            level -= 1
        return res[::-1]
