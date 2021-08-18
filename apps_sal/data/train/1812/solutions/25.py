class MajorityChecker:
    import bisect
    import random

    def __init__(self, arr: List[int]):
        self.pos = collections.defaultdict(list)
        for k, v in enumerate(arr):
            self.pos[v].append(k)
        self.runtime = 20
        self.a = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        for i in range(self.runtime):
            val = self.a[random.randint(left, right)]
            ll = bisect.bisect_left(self.pos[val], left)
            rr = bisect.bisect_right(self.pos[val], right)
            if (rr - ll) >= threshold:
                return val
        return -1
