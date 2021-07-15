class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
      self.counter_ = 0
      self.discount_ = discount
      self.max_ = n
      self.dicts_ = {}
      for i in range(len(products)):
        self.dicts_[products[i]] = prices[i]
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
      self.counter_ += 1
      bill = 0
      for i in range(len(product)):
        bill += self.dicts_[product[i]]*amount[i]
      if self.counter_ == self.max_:
        bill *= (1-self.discount_/100)
        self.counter_ = 0
      return bill
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

