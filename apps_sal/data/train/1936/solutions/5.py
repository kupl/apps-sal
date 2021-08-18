import numpy as np


class Solution:
    def parent(self, label: int) -> int:
        row = int(np.log2(label))
        counter = label - 2**row
        parent = label - (counter + int(counter / 2) + 1)
        return parent

    def pathInZigZagTree(self, label: int) -> List[int]:
        sol = []
        while True:
            sol.append(label)
            print(sol)
            if label > 1:
                label = Solution.parent(self, label)
            else:
                break
        return sol[::-1]
