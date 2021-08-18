class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.cur = 0
        self.discount = discount
        self.products = products
        self.prices = prices

    def getBill(self, product: List[int], amount: List[int]) -> float:
        temp = []
        for i in range(len(product)):
            temp.append([product[i], amount[i]])
        self.cur += 1
        result = 0
        for id, number in temp:
            real_id = self.products.index(id)
            price = self.prices[real_id]
            result += price * number
        if self.cur % self.n == 0:
            result = result * (1 - (self.discount / 100))
        return result
