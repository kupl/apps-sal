class StockSpanner:

    def __init__(self):
        self.prices = []
        self.counter = []
        

    def next(self, price: int) -> int:
        self.prices.append(price)
        length = len(self.prices)
        
        if length == 1:
            self.counter.append(1)
            
        else:
            if self.prices[-2] <= price:
                cnt = 0
                for i in range(length-self.counter[-1]-1, -1,-1):
                    if self.prices[i] <= price:
                        cnt += 1
                    else: 
                        break
                self.counter.append(self.counter[-1]+cnt)
            else:
                self.counter.append(1)
        return self.counter[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

