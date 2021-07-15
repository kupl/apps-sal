class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        # self.products = {p: i for i, p in enumerate(products)}
        self.products = products
        self.prices = prices
        
        self.counter = 0
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter += 1
        cost = sum([self.prices[self.products.index(p)] * amount[i] for i, p in enumerate(product)])
        if self.counter % self.n == 0:
            return cost - (self.discount * cost) / 100
        else:
            return cost
            


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

