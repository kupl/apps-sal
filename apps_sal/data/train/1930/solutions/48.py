class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        dicta = {}
        self.products = products
        self.prices = prices
        self.nown = n

    def getBill(self, product: List[int], amount: List[int]) -> float:
        applied = False
        if self.nown==1:
            applied = True
            self.nown = self.n
        else:
            self.nown -=1
        summoney = 0
        for i in range(len(product)):
            summoney+= self.prices[self.products.index(product[i])]*amount[i]
        if applied:
            return summoney - (summoney*self.discount)/100
        else:
            return summoney
        
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

