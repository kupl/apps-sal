class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.prices = dict(list(zip(products, prices)))
        self.discount = discount
        self.cnt = 0
        self.n = n

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        self.cnt += 1
        for i, p in enumerate(product):
            total += self.prices[p] * amount[i]

        if self.cnt % self.n == 0:
            return total * (1 - self.discount / 100)
        else:
            return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
