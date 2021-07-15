class StockSpanner:

    def __init__(self):
        self.st = []
        self.idx = 0
        

    def next(self, price: int) -> int:
        while len(self.st) and self.st[-1][0] <= price:
            self.st.pop()
        ans = self.idx - (0 if not len(self.st) else self.st[-1][1])+1
        self.st.append((price, self.idx+1))
        self.idx += 1
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

