class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.products = products
        self.prices = prices
        self.n = n
        self.i = 0
        self.discount = discount / 100

    def getBill(self, product: List[int], amount: List[int]) -> float:

        price = 0

        for p, a in zip(product, amount):
            idx = self.products.index(p)
            price += a * self.prices[idx]

        self.i += 1

        if self.i % self.n == 0:
            price -= self.discount * price

        return price


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
