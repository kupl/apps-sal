class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        import numpy as np
        arr.sort()
        # m=np.median(np.array(arr))
        m = arr[int((len(arr) - 1) / 2)]
        #sorted(arr, key=lambda x: (abs(x-median), x), reverse=True)[:k]
        a = sorted(arr, key=lambda x: (abs(x - m), x), reverse=True)
        return a[:k]
