class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.N = n
        self.count = n
        self.disc = discount
        self.p_dict = {}
        for pd,pr in zip(products,prices):
            self.p_dict[pd] = pr

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total_p = 0
        for pd,num in zip(product,amount):
            total_p += self.p_dict[pd]*num
        if self.count == 1:
            total_p = total_p*(1-self.disc/100)
            self.count = self.N
        else:
            self.count -= 1
        return total_p
    

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

