import numpy as np


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        mat = np.matrix(mat)
        indices_pack = np.where(mat == 1)
        indices = [(i, j) for i, j in zip(indices_pack[0], indices_pack[1])]
        print(indices)

        count = np.array([1 for x, y in indices if mat[x, :].sum() == 1 and mat[:, y].sum() == 1])
        return int(count.sum())
