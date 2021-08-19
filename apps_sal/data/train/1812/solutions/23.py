class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.A = arr
        self.itemIdx = collections.defaultdict(list)
        for i, x in enumerate(self.A):
            self.itemIdx[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            x = self.A[random.randint(left, right)]
            l = bisect.bisect_left(self.itemIdx[x], left)
            r = bisect.bisect_right(self.itemIdx[x], right)
            if r - l >= threshold:
                return x
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
