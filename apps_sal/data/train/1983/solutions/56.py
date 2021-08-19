class ProductOfNumbers:

    def __init__(self):
        self.hash = {}

    def add(self, num: int) -> None:
        curr = len(self.hash)
        if num == 0:
            self.hash[curr] = (curr, 1)
        else:
            product = 1 if curr == 0 or self.hash[curr - 1][1] == 0 else self.hash[curr - 1][1]
            prev = self.hash[curr - 1][0] if len(self.hash) else -1
            self.hash[curr] = (prev, product * num)

    def getProduct(self, k: int) -> int:
        prev = self.hash[len(self.hash) - 1][0]
        low, up = (len(self.hash) - 1) - k + 1, len(self.hash) - 1
        if low <= prev <= up:
            return 0
        top = len(self.hash) - 1 - k
        end = len(self.hash) - 1
        return int(self.hash[end][1] / self.hash[top][1]) if k != len(self.hash) else self.hash[k - 1][1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
