class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.idxes = collections.defaultdict(list)
        for (i, n) in enumerate(arr):
            self.idxes[n].append(i)
        self.arr = arr
        self.st = SegmentTree(len(arr), arr, self.idxes)

    def query(self, left: int, right: int, threshold: int) -> int:
        maj = self.st.query_maj(left, right)
        if maj:
            l, r = bisect.bisect_left(self.idxes[maj], left), bisect.bisect(self.idxes[maj], right)
            if r - l >= threshold:
                return maj
        return -1


class SegmentTree:

    def __init__(self, n, arr, idxes):
        self.root = Node(0, n - 1, arr, idxes)

    def query_maj(self, lo, hi):
        return self.root.query_maj(lo, hi)


class Node:

    def __init__(self, lo, hi, arr, idxes):
        self.lo, self.hi = lo, hi
        self.lc, self.rc = None, None
        self.arr, self.idxes = arr, idxes
        self.maj = None

    def query_maj(self, lo, hi):

        def is_maj(n):
            if not n:
                return False

            l = bisect.bisect_left(self.idxes[n], lo)
            r = bisect.bisect(self.idxes[n], hi)
            return (r - l << 1) > hi - lo

        if lo > hi or self.lo > hi or self.hi < lo:
            return None

        if self.lo >= lo and self.hi <= hi:
            if not self.maj:
                if self.lo == self.hi:
                    self.maj = self.arr[self.lo]
                else:
                    mi = (self.lo + self.hi) >> 1
                    if not self.lc:
                        self.lc = Node(self.lo, mi, self.arr, self.idxes)
                    if not self.rc:
                        self.rc = Node(mi + 1, self.hi, self.arr, self.idxes)
                    l = self.lc.query_maj(self.lo, mi)
                    r = self.rc.query_maj(mi + 1, self.hi)
                    self.maj = l if is_maj(l) else r if is_maj(r) else -1
            return self.maj

        mi = (self.lo + self.hi) >> 1
        if not self.lc:
            self.lc = Node(self.lo, mi, self.arr, self.idxes)
        if not self.rc:
            self.rc = Node(mi + 1, self.hi, self.arr, self.idxes)

        l = self.lc.query_maj(lo, hi)
        r = self.rc.query_maj(lo, hi)
        return l if is_maj(l) else r if is_maj(r) else -1
