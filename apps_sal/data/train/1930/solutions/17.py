class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.count = 0
        self.discount_factor = 1 - discount / 100
        self.prices_dict = {}
        for product, price in zip(products, prices):
            self.prices_dict[product] = price

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        discount_factor = 1
        if self.count == self.n:
            discount_factor = self.discount_factor
            self.count = 0
        price_sum = 0.
        for p, a in zip(product, amount):
            price_sum += a * self.prices_dict[p]
        return discount_factor * price_sum
