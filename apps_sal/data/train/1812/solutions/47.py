import numpy as np


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = np.array(arr)

    def query(self, left: int, right: int, threshold: int) -> int:
        count = np.bincount(self.arr[left:right + 1])
        x = np.argmax(count)
        if count[x] >= threshold:
            return x
        return -1
