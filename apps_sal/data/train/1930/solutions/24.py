class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.productToId = {product: productId for productId, product in enumerate(products)}
        self.productIdToPrice = {productId: price for productId, price in enumerate(prices)}
        self.customerNumber = 0

    def calculateCost(self, productsBought: List[int], amounts: List[int]) -> float:
        cost = 0

        for i in range(len(productsBought)):
            product, productAmount = productsBought[i], amounts[i]
            price = self.getProductPrice(product)
            cost += price * productAmount

        return cost

    def calculateDiscountedCost(self, cost: float) -> float:
        return cost - (self.discount * cost) / 100

    def getProductPrice(self, product: int) -> int:
        return self.productIdToPrice[self.productToId[product]]

    def getBill(self, productsBought: List[int], amounts: List[int]) -> float:
        self.customerNumber += 1

        cost = self.calculateCost(productsBought, amounts)

        if self.customerNumber == self.n:
            cost = self.calculateDiscountedCost(cost)
            self.customerNumber = 0

        return cost
