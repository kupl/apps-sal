class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.x_idxs = x_idxs = defaultdict(list)
        for i, x in enumerate(arr):
            x_idxs[x].append(i)
        self.xs = sorted(list(x_idxs.keys()), key=lambda x: -len(x_idxs[x]))

    def query(self, left: int, right: int, threshold: int) -> int:
        for x in self.xs:
            idxs = self.x_idxs[x]
            if len(idxs) < threshold:
                break
            r = bisect.bisect_right(idxs, right)
            l = bisect.bisect_right(idxs, left - 1)
            if r - l >= threshold:
                return x
        return -1
