class MajorityChecker:
    # copied https://leetcode.com/problems/online-majority-element-in-subarray/discuss/355848/Python-Binary-Search-%2B-Find-the-Majority-Element

    def __init__(self, arr: List[int]):
        a2i = collections.defaultdict(list)
        for i, x in enumerate(arr):
            a2i[x].append(i)
        self.A, self.a2i = arr, a2i

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            a = self.A[random.randint(left, right)]
            l = bisect.bisect_left(self.a2i[a], left)
            r = bisect.bisect_right(self.a2i[a], right)
            if r - l >= threshold:
                return a
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
