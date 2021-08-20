import random


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.fre = {i: [] for i in set(arr)}
        for i in range(len(arr)):
            self.fre[arr[i]].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(50):
            i = left + random.randint(0, right - left)
            low = self.bs(self.fre[self.arr[i]], left)
            if self.fre[self.arr[i]][low] < left:
                low += 1
            high = self.bs(self.fre[self.arr[i]], right)
            if high - low + 1 >= threshold:
                return self.arr[i]
        return -1

    def bs(self, arr, n):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = low + (high - low + 1) // 2
            if arr[mid] <= n:
                low = mid
            else:
                high = mid - 1
        return low
