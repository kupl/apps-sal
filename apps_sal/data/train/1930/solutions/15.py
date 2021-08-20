class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.mapping = {}
        for i in range(len(prices)):
            self.mapping[products[i]] = prices[i]
        self.customer = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer += 1
        total = 0.0
        for i in range(len(product)):
            total += self.mapping[product[i]] * amount[i]
        if self.customer % self.n == 0:
            total = total - self.discount / 100 * total
        return total
