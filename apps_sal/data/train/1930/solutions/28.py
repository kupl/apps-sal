class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.index = 0
        self.prices = collections.defaultdict(int)
        for i in range(len(products)):
            self.prices[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.index += 1
        total = sum([self.prices[product[i]] * amount[i] for i in range(len(product))])
        if self.index % self.n == 0:
            total = (1 - self.discount / 100) * total
        return float(total)
