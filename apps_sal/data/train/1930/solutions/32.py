class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.product_price = {}
        self.current = 0
        for i in range(len(products)):
            self.product_price[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.current+=1
        total = 0
        for i in range(len(product)):
            total = total + (self.product_price[product[i]] * amount[i])
        
        if(self.current == self.n):
            self.current = 0
            total = total * (1 - self.discount/100)
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

