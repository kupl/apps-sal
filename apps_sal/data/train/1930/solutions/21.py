class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.count = 0
        self.price_dict = {}
        for i, item in enumerate(products):
            self.price_dict[item] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = .0
        self.count += 1
        for i, idx in enumerate(product):
            total += amount[i] * self.price_dict[idx]

        if self.count % self.n == 0 and self.count > 0:
            total -= total * self.discount / 100.0

        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
