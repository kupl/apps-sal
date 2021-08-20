class Solution:

    def pathInZigZagTree(self, label: int):
        out = []
        while label >= 1:
            out.append(label)
            label = self.swap(label)
        return out[::-1]

    def swap(self, x):
        to = 1
        while to <= x:
            to = to << 1
        return (to + (to >> 1) - 1 - x) // 2
