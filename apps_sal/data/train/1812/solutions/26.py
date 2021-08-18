class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.N = len(arr)
        self.max_len = 1 << ceil(log2(self.N)) + 1
        self.seg = [None] * self.max_len
        self.seg_build(1, 0, self.N - 1, arr)
        self.indices = defaultdict(list)
        for i, a in enumerate(arr):
            self.indices[a].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        def bs(arr, l, r, target):
            while l <= r:
                m = l + (r - l) // 2
                if arr[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r

        major = self.seg_query(1, 0, self.N - 1, left, right)[0]
        lst = self.indices[major]
        l, r = bs(lst, 0, len(lst) - 1, left - 1), bs(lst, 0, len(lst) - 1, right)
        if r - l >= threshold:
            return major
        return -1

    def seg_build(self, idx, s, e, arr):
        if s == e:
            self.seg[idx] = [arr[s], 1]
            return

        mid = s + (e - s) // 2
        self.seg_build(2 * idx, s, mid, arr)
        self.seg_build(2 * idx + 1, mid + 1, e, arr)
        self.seg[idx] = self.merge(self.seg[2 * idx], self.seg[2 * idx + 1])

    def seg_query(self, idx, s, e, l, r):
        if s >= l and e <= r:
            return self.seg[idx]

        if s > r or e < l:
            return [0, 0]

        mid = s + (e - s) // 2
        return self.merge(self.seg_query(2 * idx, s, mid, l, r), self.seg_query(2 * idx + 1, mid + 1, e, l, r))

    def merge(self, A, B):
        lv, lf = A
        rv, rf = B
        if lv == rv:
            return [lv, lf + rf]
        else:
            if lf > rf:
                return [lv, lf - rf]
            else:
                return [rv, rf - lf]
