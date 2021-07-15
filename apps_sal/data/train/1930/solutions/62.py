class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n=n
        self.dic={}
        for x,y in zip(products,prices):
            self.dic[x]=y
        self.dis=discount
        self.k=0
    
    def getBill(self, product: List[int], amount: List[int]) -> float:
        total=0
        for x,y in zip(product,amount):
            total+=self.dic[x]*y
            
        self.k+=1
        if self.k==self.n:
            self.k=0
            return total-(total*(self.dis/100.0))
            
        else:
            return total
        
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

