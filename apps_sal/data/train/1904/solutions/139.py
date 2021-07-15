from numpy import argsort
from numpy import array
from numpy import sqrt
from numpy import sum

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        p = array(points)
        q = sqrt(sum(p ** 2, axis=1))
        return p[argsort(q)[:K]]
