class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.num_disc = n
        self.disc = discount
        self.prod = products
        self.pric = prices
        self.count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        total = 0
        for i in range(len(product)):
            ind = self.prod.index(product[i])
            total += (self.pric[ind] * amount[i])
        if(self.count != 0 and self.count % self.num_disc == 0):
            total = (total - (self.disc * total) / 100)
            self.count = 0
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
