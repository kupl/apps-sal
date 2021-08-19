class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.indices = defaultdict(list)
        for a in set(arr):
            self.indices[a].append(-1)
        for i, a in enumerate(arr):
            self.indices[a].append(i)
        self.a = list(self.indices.keys())

    def query(self, left: int, right: int, threshold: int) -> int:
        def bs(arr, l, r, target):
            while l <= r:
                m = l + (r - l) // 2
                if arr[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r

        for _ in range(20):
            a = random.choice(self.a)
            lst = self.indices[a]
            l, r = bs(lst, 0, len(lst) - 1, left - 1), bs(lst, 0, len(lst) - 1, right)
            if r - l >= threshold:
                return a

        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
