import numpy as np


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        p = np.array(points)
        q = np.sqrt(np.sum(p ** 2, axis=1))
        return p[np.argsort(q)[:K]]
