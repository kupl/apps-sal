from collections import defaultdict
from bisect import bisect_left, bisect_right


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.el_to_idx = defaultdict(list)

        for i, val in enumerate(arr):
            self.el_to_idx[val].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        N = 10
        for _ in range(N):
            val = self.arr[random.randint(left, right)]
            indices = self.el_to_idx[val]
            lo = bisect_left(indices, left)
            hi = bisect_right(indices, right)

            if hi - lo >= threshold:
                return val
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
