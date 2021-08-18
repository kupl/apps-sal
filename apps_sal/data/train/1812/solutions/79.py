from bisect import bisect_left, bisect_right


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.dic = defaultdict(list)
        for i, e in enumerate(arr):
            self.dic[e].append(i)
        self.nums = sorted(self.dic, key=lambda x: len(self.dic[x]), reverse=True)

    def query(self, left: int, right: int, threshold: int) -> int:
        for num in self.nums:
            entry = self.dic[num]
            if len(entry) < threshold:
                return -1
            l, r = bisect_left(entry, left), bisect_right(entry, right)
            if r - l >= threshold:
                return num
        return -1
