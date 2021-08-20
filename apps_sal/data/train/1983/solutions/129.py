class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.ZeroIdx = []

    def add(self, num: int) -> None:
        n = len(self.arr)
        if num == 0:
            self.ZeroIdx.append(n)
            num = 1
        if n == 0:
            self.arr.append(num)
        else:
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        if k == 0:
            return 0
        n = len(self.arr)
        for idx in self.ZeroIdx:
            if idx >= n - k:
                return 0
        n = len(self.arr)
        if n == k:
            return self.arr[n - 1]
        else:
            return self.arr[n - 1] // self.arr[n - k - 1]
