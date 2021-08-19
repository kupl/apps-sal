class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.counter = 0
        self.period = n
        self.discount = 1 - discount / 100
        self.prices = {}
        for index, productId in enumerate(products):
            self.prices[productId] = prices[index]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter += 1
        totalAmount = 0
        for index, productId in enumerate(product):
            totalAmount += self.prices[productId] * amount[index]
        if self.counter % self.period == 0:
            totalAmount = self.discount * totalAmount
        return totalAmount

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
