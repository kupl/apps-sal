import math


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        def findIndexorLabel(value):
            level = int(math.log(value, 2)) + 1
            if level % 2:
                index = value
            else:
                total = 2**(level - 1) + (2**level - 1)
                index = total - value
            return index
        arr = []
        arr.insert(0, label)
        index = findIndexorLabel(label)
        parentNode = index // 2
        while parentNode != 0:
            nodeVal = findIndexorLabel(parentNode)
            arr.insert(0, nodeVal)
            index = findIndexorLabel(nodeVal)
            parentNode = index // 2
        return arr
