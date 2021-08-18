class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.product_to_price = dict(list(zip(products, prices)))
        self.discount = discount / 100
        self.n = n
        self.cur_customer = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        prices = [self.product_to_price[prod] * amt for prod, amt in zip(product, amount)]
        self.cur_customer += 1
        disc = self.discount if self.cur_customer % self.n == 0 else 0

        return sum(prices) * (1 - disc)
