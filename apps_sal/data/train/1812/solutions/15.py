from collections import defaultdict
from bisect import bisect_left, bisect_right


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.el_to_idx = defaultdict(list)

        for i, val in enumerate(arr):
            self.el_to_idx[val].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        N = 15
        for _ in range(15):
            val = self.arr[random.randint(left, right)]
            indices = self.el_to_idx[val]
            lo = bisect_left(indices, left)
            hi = bisect_right(indices, right)

            if hi - lo >= threshold:
                return val
        return -1
