class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.count = 0
        self.n = n
        self.discount = discount
        self.products = {}
        
        for i in range(len(products)):
            self.products[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        cost = 0
        
        for pr, am in zip(product, amount):
            cost += self.products[pr] * am
        if self.count % self.n == 0:
            self.count = 0
            return cost * (1 - self.discount/100)
        return cost


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

