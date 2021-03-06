import bisect


class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.zero_idx = []

    def add(self, num: int) -> None:
        n = len(self.arr)
        if num == 0:
            self.arr = [0] * (n + 1)
            self.zero_idx.append(n)
        elif n == 0 or self.arr[-1] == 0:
            self.arr.append(num)
        else:
            self.arr.append(num * self.arr[-1])

    def getProduct(self, k: int) -> int:
        i = len(self.arr) - k
        x = bisect.bisect_right(self.zero_idx, i - 1, 0, len(self.zero_idx))
        if x == len(self.zero_idx):
            if k == len(self.arr):
                return self.arr[-1]
            else:
                if self.arr[len(self.arr) - k - 1]:
                    return self.arr[-1] // self.arr[len(self.arr) - k - 1]
                return self.arr[-1]
        else:
            return 0
