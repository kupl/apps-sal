class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.N = n
        self.count = 0
        self.discount = discount
        self.products = products
        self.prices = prices
        self.reverse_dict = {i: j for (j, i) in enumerate(products)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        price_total = 0
        for (i, am) in zip(product, amount):
            price_total += am * self.prices[self.reverse_dict[i]]
        self.count += 1
        if self.count >= self.N:
            price_total *= 1 - self.discount / 100.0
            self.count = 0
        return price_total
