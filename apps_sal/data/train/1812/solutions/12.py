class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.idxes = collections.defaultdict(list)
        for (i, n) in enumerate(arr):
            self.idxes[n].append(i)
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(10):
            n = self.arr[random.randint(left, right)]
            l = bisect.bisect_left(self.idxes[n], left)
            r = bisect.bisect_right(self.idxes[n], right)
            if r - l >= threshold:
                return n
        return -1
    
# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

