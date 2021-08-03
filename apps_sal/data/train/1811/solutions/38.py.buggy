class StockSpanner:

    def __init__(self):
        self.day = 1
        self.ascendingStack = [(0, float(\"inf\"))]
    
    def next(self, price: int) -> int:
        while self.ascendingStack[-1][1] <= price:
            self.ascendingStack.pop()
            
        days = self.day - self.ascendingStack[-1][0]
        self.ascendingStack.append((self.day, price))
        self.day+=1
        
        return days

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
