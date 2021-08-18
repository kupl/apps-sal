class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = {}
        for idx, item in enumerate(products):
            self.products[item] = prices[idx]
        self.count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        bill = 0
        for idx, item in enumerate(product):
            bill += self.products[item] * amount[idx]
        if self.count % self.n == 0:
            return ((100 - self.discount) / 100) * bill
        else:
            return bill
