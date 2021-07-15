class StockSpanner:


    def __init__(self):
        
        self.stack = []
        self.ind = 0
        self.vals = []

    def next(self, price):

        #print(price, self.stack, self.ind, self.vals)
        
        self.vals+=[price]
        
        while len(self.stack)>0 and self.vals[self.stack[-1]]<=price:
            self.stack.pop()

        if len(self.stack)>0:
            res = self.ind - self.stack[-1]
        else:
            res = self.ind+1

        self.stack+=[self.ind]

        self.ind+=1
        
        #print(\"at end \", price, self.stack, self.ind, self.vals)

        if self.ind==1:
            return 1

        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

