from bisect import bisect_left, bisect_right


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.dic = defaultdict(list)
        for i, e in enumerate(arr):
            self.dic[e].append(i)
        self.nums = sorted(self.dic, key=lambda x: len(self.dic[x]), reverse=True)

    def query(self, left: int, right: int, threshold: int) -> int:
        # try all nums
        # 1 2 4 6
        # 1 4
        # see how many times each appears in range
        for num in self.nums:
            # find where first and last occurrence are
            entry = self.dic[num]
            if len(entry) < threshold:
                return -1
            l, r = bisect_left(entry, left), bisect_right(entry, right)
            if r - l >= threshold:
                return num
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
