class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.count = 0
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        total = 0
        for i in range(len(product)):
            total += amount[i] * self.prices[self.products.index(product[i])]
        if self.count % self.n == 0:
            total = total - self.discount * total / 100
            return total
        return total
