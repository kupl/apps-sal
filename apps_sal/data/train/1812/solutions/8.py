from math import log2


class Node:

    def __init__(self, val, freq):
        self.val = val
        self.freq = freq


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.locations = {}
        for (i, val) in enumerate(arr):
            if val in self.locations:
                self.locations[val].append(i)
            else:
                self.locations[val] = [i]
        self.occur = sorted(list(self.locations.items()), reverse=True, key=lambda x: len(x[1]))
        print(self.occur)

    def lower_bound(self, arr, x):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + r >> 1
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def upper_bound(self, arr, x):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + r >> 1
            if arr[mid] <= x:
                l = mid + 1
            else:
                r = mid - 1
        return r + 1

    def query(self, left: int, right: int, threshold: int) -> int:
        for (i, j) in self.occur:
            if len(j) < threshold:
                return -1
            s = self.lower_bound(j, left)
            e = self.upper_bound(j, right)
            if e - s >= threshold:
                return i
        return -1
