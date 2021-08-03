class StockSpanner:
    \"\"\"
    Solution:
        1. use a stack to store the current max price, and the corresponding span
        2. comprare the comming price, and merge to the stack if needed
    Time complexity: O(n)
    Space complexity: O(n) if the span is always 1
    \"\"\"
    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price, 1])
            return self.stack[-1][1]
        count = 1
        while self.stack and price >= self.stack[-1][0]:
            count += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, count])
        
        return self.stack[-1][1]
            
        
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
