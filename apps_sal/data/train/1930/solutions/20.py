class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.count = 0
        self.propri = {}
        self.discount = discount
        for i in range(len(products)):
            self.propri[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        discount_flag = False
        if self.count % self.n == 0:
            discount_flag = True

        result = 0

        for i in range(len(product)):
            result += self.propri[product[i]] * amount[i]

        if discount_flag:
            result *= (100 - self.discount) / 100

        return result


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
