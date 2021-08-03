class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        a2i = collections.defaultdict(list)
        for i, a in enumerate(arr):
            a2i[a].append(i)

        self.a2i = a2i

    def query(self, left: int, right: int, threshold: int) -> int:

        for _ in range(16):
            a = self.arr[random.randint(left, right)]
            l = bisect.bisect_left(self.a2i[a], left)
            r = bisect.bisect_right(self.a2i[a], right)
            if r - l >= threshold:
                return a
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
