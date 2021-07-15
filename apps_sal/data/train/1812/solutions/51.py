class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.x_idxs = x_idxs = defaultdict(list)

        for i, x in enumerate(arr):
            x_idxs[x].append(i)

        self.xs = sorted(list(x_idxs.keys()), key=lambda x: -len(x_idxs[x]))

    def query(self, left: int, right: int, threshold: int) -> int:
        br = bisect.bisect_right
        for x in self.xs:
            idxs = self.x_idxs[x]
            if len(idxs) < threshold:
                break
            if br(idxs, right) - br(idxs, left - 1) >= threshold:
                return x

        return -1
    

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

