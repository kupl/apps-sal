from collections import deque

class ProductOfNumbers:

    def __init__(self):
        self.q = deque()
        self.running_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.q = deque()
            self.running_products = [1]
        else:
            self.running_products.append(self.running_products[-1] * num)
            self.q.append(num)        

    def getProduct(self, k: int) -> int:
        if len(self.q) < k:
            return 0
        return int(self.running_products[-1] / self.running_products[-k - 1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

