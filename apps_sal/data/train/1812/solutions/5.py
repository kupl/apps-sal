class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.indices = defaultdict(list)
        for a in set(arr):
            self.indices[a].append(-1)
        for i, a in enumerate(arr):
            self.indices[a].append(i)
        self.A = sorted(list(self.indices.keys()), key=lambda x: -len(self.indices[x]))

    def query(self, left: int, right: int, threshold: int) -> int:
        def bs(arr, l, r, target):
            while l <= r:
                m = l + (r - l) // 2
                if arr[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r

        for a in self.A:
            lst = self.indices[a]
            if len(lst) < threshold:
                return -1
            l, r = bs(lst, 0, len(lst) - 1, left - 1), bs(lst, 0, len(lst) - 1, right)
            if r - l >= threshold:
                return a

        return -1
