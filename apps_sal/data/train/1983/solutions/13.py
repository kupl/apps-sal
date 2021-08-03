class ProductOfNumbers:

    def __init__(self):
        self.n = 0
        self.d = {}

    def add(self, num: int) -> None:
        n = self.n
        self.d[(n, n)] = num
        self.n += 1

    def getProduct(self, k: int) -> int:
        return self.h(self.n - k, self.n - 1)

    def h(self, i, j):
        d = self.d
        h = self.h
        if (i, j) in d:
            return d[(i, j)]
        m = (i + j) // 2
        x = h(i, m) * h(m + 1, j)
        d[(i, j)] = x
        return x

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
