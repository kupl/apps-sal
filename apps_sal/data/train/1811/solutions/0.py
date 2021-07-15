class StockSpanner:

    def __init__(self):
        self.s=[]
        

    def next(self, price: int) -> int:
        stk=self.s
        curr_span=1
        
        while stk and stk[-1][0]<=price: #curr_price is > stack[-1][0]
            prev_price,prev_span=stk.pop()
            curr_span+=prev_span
        stk.append((price,curr_span))
        return curr_span
            
            
        
            
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

