class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.client = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.client += 1
        bill = 0
        for (p, a) in zip(product, amount):
            idx = self.products.index(p)
            bill += a * self.prices[idx]
        if self.client == self.n:
            self.client = 0
            bill = bill - self.discount * bill / 100
        return bill
