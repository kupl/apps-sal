class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customer = 0
        self.n = n
        self.discount = discount / 100
        self.h = {}
        for i in range(len(products)):
            self.h[products[i]] = prices[i]
        
    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer += 1

        total = 0
        for i in range(len(product)):
            total += self.h[product[i]] * amount[i]
        
        if self.customer == self.n:
            self.customer = 0
            return total - (self.discount * total)
        
        else:
            return total

