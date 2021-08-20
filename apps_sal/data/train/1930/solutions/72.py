class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.top = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.top += 1
        bill = 0
        for (i, p) in enumerate(product):
            index = self.products.index(p)
            cost = self.prices[index]
            total = cost * amount[i]
            bill += total
        if self.top == self.n:
            bill -= self.discount * bill / 100
            self.top = 0
        return bill
