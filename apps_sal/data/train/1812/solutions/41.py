class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.x_idxs = x_idxs = defaultdict(list)
        for i, x in enumerate(arr):
            x_idxs[x].append(i)
        self.xs = sorted((len(idxs), x) for x, idxs in list(x_idxs.items()))[::-1]

    def query(self, left: int, right: int, threshold: int) -> int:
        for length, x in self.xs:
            if length < threshold:
                break
            idxs = self.x_idxs[x]
            r = bisect.bisect_right(idxs, right)
            l = bisect.bisect_right(idxs, left - 1)
            if r - l >= threshold:
                return x
        return -1

    

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

