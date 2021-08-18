class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.count = 0
        self.discount = discount
        self.products = products.copy()
        self.prices = prices.copy()

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        bill = 0
        for quantity, pid in zip(amount, product):
            index = self.products.index(pid)
            bill += self.prices[index] * quantity
        if self.count == self.n:
            bill = bill - ((self.discount * bill) / 100)
            self.count = 0
        return bill
