class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.memo = collections.defaultdict(list)
        for i, x in enumerate(arr):
            self.memo[x].append(i)
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            r = self.arr[random.randint(left, right)]
            lo = bisect.bisect_left(self.memo[r], left)
            hi = bisect.bisect_right(self.memo[r], right)
            if hi - lo >= threshold:
                return r
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
