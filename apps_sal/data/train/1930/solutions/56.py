class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.customer = 1

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        for i in range(len(product)):
            ids = self.products.index(product[i])
            bill += self.prices[ids] * amount[i]
        if self.customer % self.n == 0:
            bill = bill - self.discount * bill / 100
        self.customer += 1
        return bill
