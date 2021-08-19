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
            low = self.bsl(self.fre[self.arr[i]], left)
            high = self.bsr(self.fre[self.arr[i]], right)
            if low == -1 or high == -1:
                continue
            if high - low + 1 >= threshold:
                return self.arr[i]
        return -1

    def bsl(self, arr, n):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] >= n:
                high = mid
            else:
                low = mid + 1
        if arr[low] >= n:
            return low
        return -1

    def bsr(self, arr, n):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = low + (high - low + 1) // 2
            if arr[mid] > n:
                high = mid - 1
            else:
                low = mid
        if arr[low] <= n:
            return low
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
