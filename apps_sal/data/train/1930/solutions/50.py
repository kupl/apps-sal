class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discountNumber = n
        self.discount = discount
        self.productsList = products
        self.pricesList = prices
        self.currentCustNum = 1

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cost = 0
        for i in range(0, len(product)):
            self.priceIndex = self.productsList.index(product[i])
            self.cost += (self.pricesList[self.priceIndex] * amount[i])
        if self.currentCustNum == self.discountNumber:
            self.cost = self.cost - ((self.discount * self.cost) / 100)
            self.currentCustNum = 1
        else:
            self.currentCustNum += 1
        return self.cost

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

