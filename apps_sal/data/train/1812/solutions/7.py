from collections import defaultdict


class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.idx = defaultdict(list)
        counts = dict()
        for i, v in enumerate(arr):
            self.idx[v].append(i)
            counts[v] = len(self.idx[v])
        self.counts = list(counts.items())
        self.counts.sort(key=lambda x: x[1], reverse=True)

    def query(self, left: int, right: int, threshold: int) -> int:
        for val, count in self.counts:
            if count < threshold:
                break
            indices = self.idx[val]
            start = find_closest(indices, left, lower=False)
            end = find_closest(indices, right, lower=True)
            n_in_range = end - start + 1
            if n_in_range >= threshold:
                return val
        return -1


def find_closest(a: List[int], target: int, lower: bool) -> int:
    low = 0
    high = len(a) - 1

    while low <= high:
        m = (low + high) // 2
        if a[m] == target:
            return m
        if a[m] < target:
            low = m + 1
        else:
            high = m - 1

    if lower:
        return high
    return low
