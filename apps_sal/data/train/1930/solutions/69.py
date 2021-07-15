class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.productToId = {product: productId for productId, product in enumerate(products)}
        self.productIdToPrice = {productId: price for productId, price in enumerate(prices)}
        self.customerNumber = 0
    def calculateCost(self, products: List[int], amounts: List[int]) -> float:
        cost = 0
        
        for i in range(len(products)):
            product, productAmount = products[i], amounts[i]
            price = self.getProductPrice(product)
            cost += price * productAmount   
        
        return cost
        
    def calculateDiscountedCost(self, cost: float) -> float:
        return cost - (self.discount * cost) / 100
    
    def getProductPrice(self, product: int) -> int:
        return self.productIdToPrice[self.productToId[product]]
        
    def getBill(self, products: List[int], amounts: List[int]) -> float:
        self.customerNumber += 1
        
        cost = self.calculateCost(products, amounts)
        
        if self.customerNumber == self.n:
            cost = self.calculateDiscountedCost(cost)
            self.customerNumber = 0
            
        return cost
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

