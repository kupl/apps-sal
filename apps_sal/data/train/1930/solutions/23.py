class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.counter = 0
        self.d = {}
        self.discount = discount
        self.n = n

        for i, x in enumerate(products):
            self.d[x] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:

        total = 0
        for i, productId in enumerate(product):
            total += self.d[productId] * amount[i]

        self.counter += 1
        if self.counter % self.n == 0:
            total = total - ((self.discount * total) / 100)

        return total
