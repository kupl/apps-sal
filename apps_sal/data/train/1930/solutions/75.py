class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.currCustomer = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.currCustomer += 1
        currBill = 0
        for i in range(len(product)):
            currBill += self.prices[self.products.index(product[i])] * amount[i]
        if (self.currCustomer == self.n):
            currBill = currBill - ((self.discount * currBill) / 100)
            self.currCustomer = 0
        return currBill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
