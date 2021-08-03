class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.indices = collections.defaultdict(list)
        for i, n in enumerate(arr):
            self.indices[n].append(i)
        self.nums = sorted(list(self.indices.keys()), key=lambda i: -1 * len(self.indices[i]))

    def query(self, left: int, right: int, threshold: int) -> int:
        for n in self.nums:
            if len(self.indices[n]) < threshold:
                return -1
            l, r = bisect.bisect_left(self.indices[n], left), bisect.bisect_right(self.indices[n], right)
            if r - l >= threshold:
                return n
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
