class MajorityChecker:

    def __init__(self, arr: List[int]):
        d = collections.defaultdict(list)
        for j, x in enumerate(arr):
            d[x].append(j)
        self.arr, self.d = arr, d

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            a = self.arr[random.randint(left, right)]
            l = bisect.bisect_left(self.d[a], left)
            r = bisect.bisect_right(self.d[a], right)
            if r - l >= threshold:
                return a
        return -1




# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

