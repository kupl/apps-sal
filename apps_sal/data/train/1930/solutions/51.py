class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n ,self.c , self.discount , self.d = n , n , 1 - discount/100 , {}
        for i in range(len(products)):
            self.d[products[i]] = prices[i]
    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        for i , v in enumerate(product):
            bill += self.d[v]*amount[i]
        self.n -= 1
        if self.n == 0:bill *= self.discount;self.n = self.c
        return bill


