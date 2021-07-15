class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        # stack, almost by myself. Idea is simple. Brute force - store prices in stack, and at every new price iterate all over stack. Innefficient!
        # But we could push to stack price and how much times we occured smaller values. For example, no need to store in stack [1,2,3,4,13], just store stack[13: 5] - and if next price would be greater than 13 - maybe 40 - we just pop 13,5 from stack and append 5 to result. Then push [40,6] to stack
        # monotonically decreasing stack?
        # good explanation here - https://leetcode.com/problems/online-stock-span/discuss/168311/C%2B%2BJavaPython-O(1)
        result = 1
        while self.stack and self.stack[-1][0] <= price:
            previous_calculated_result = self.stack.pop()[1]
            result += previous_calculated_result

        self.stack.append([price, result])
        print((self.stack))
        return result
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

