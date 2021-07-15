class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.crCustomer = 0
        self.dic_prices = dict(list(zip(products, prices)))

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.crCustomer+=1
        if self.crCustomer % self.n == 0:
            discount =  self.discount
        else:
            discount = 0
                 
        return sum([ (1- discount/100) * self.dic_prices[p]*a for p,a in zip(product, amount)])
            
            
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

