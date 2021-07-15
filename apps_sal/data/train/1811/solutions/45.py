class StockSpanner:

    def __init__(self):
        # from collections import defaultdict
        self.Dict = defaultdict(int)
        self.s = []
        self.count = 0
    def next(self, price: int) -> int:
        if len(self.s) == 0:
            self.s.append((self.count, price))
            self.Dict[(self.count, price)] += 1
            ans = self.Dict[(self.count, price)]
            self.count += 1
            return ans
        else:
            while len(self.s) != 0 and price >= self.s[-1][1]:
                self.Dict[(self.count, price)] += self.Dict[(self.s[-1][0], self.s[-1][1])] 
                self.s.pop(-1)
            self.s.append((self.count, price))
            self.Dict[(self.count, price)] += 1
            ans = self.Dict[(self.count, price)]
            self.count += 1
            return ans
            
                
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

