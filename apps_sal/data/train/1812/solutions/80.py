class MajorityChecker:

    def __init__(self, arr: List[int]):

        self.idx = collections.defaultdict(list)
        for i, a in enumerate(arr):
            self.idx[a].append(i)

        print((self.idx))

    def query(self, left: int, right: int, threshold: int) -> int:

        for k, v in list(self.idx.items()):
            l = bisect.bisect_left(v, left)
            r = bisect.bisect_right(v, right)
            if r - l >= threshold:
                return k

        return -1
