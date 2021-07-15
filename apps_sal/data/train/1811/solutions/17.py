class StockSpanner:

    def __init__(self):
        self.stack = [[0,1]]   
    def next(self, price: int) -> int:
        if price < self.stack[-1][0]:
            self.stack.append([price,1])
            return 1
        else:
            days = 0
            while self.stack and price >= self.stack[-1][0]:
                p, d = self.stack.pop()
                days += d # stack previous days
            try:
                days +=self.stack[-1][1] 
                self.stack[-1][1] = days # insert
            except:
                self.stack.append([0,days])
            self.stack.append([price,1])
        return days
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

