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

        if lo <= self.lo <= self.hi <= hi:
            if not self.maj:
                if self.lo == self.hi:
                    self.maj = self.arr[self.lo]
                else:
                    l, r = None, None
                    mi = (self.lo + self.hi) >> 1
                    # Note: we don't need to check whether 'lc' or 'rc' overlap with [lo, hi],
                    # since the parent node is already within [lo, hi]
                    if not self.lc:
                        self.lc = Node(self.lo, mi, self.arr, self.idxes)
                    # Note: we should not query [lo, hi], but instead query [self.lo, mi],
                    # since maj element in [self.lo, mi] may not necessarily be a maj element of [lo, hi],
                    # leading to a false negative
                    l = self.lc.query_maj(self.lo, mi)

                    # Note: same on the 'rc' as on 'lc'
                    if not self.rc:
                        self.rc = Node(mi + 1, self.hi, self.arr, self.idxes)
                    r = self.rc.query_maj(mi + 1, self.hi)

                    self.maj = l if is_maj(l) else r if is_maj(r) else -1
            return self.maj

        mi = (self.lo + self.hi) >> 1
        l, r = None, None
        if lo <= mi:
            if not self.lc:
                self.lc = Node(self.lo, mi, self.arr, self.idxes)
            l = self.lc.query_maj(max(self.lo, lo), min(mi, hi))
        if mi + 1 <= hi:
            if not self.rc:
                self.rc = Node(mi + 1, self.hi, self.arr, self.idxes)
            r = self.rc.query_maj(max(lo, mi + 1), min(self.hi, hi))
        return l if is_maj(l) else r if is_maj(r) else -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
