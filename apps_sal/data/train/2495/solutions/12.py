class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        import numpy as np
        return((np.sort(target) == np.sort(arr)).all())
