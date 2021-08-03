class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, data: int):
        self.stack.append(data)

    def pop(self) -> int:
        if self.isEmpty():
            return \"No element in the Stack\"
        else:
            return self.stack.pop()

    def top(self) -> int:
        if self.isEmpty():
            return (\"No element in the Stack\")
        else:
            return self.stack[-1]

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

class StockSpanner:

    def __init__(self):
        self.maxStack = MyStack()
        self.nums = []
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        while not self.maxStack.isEmpty() and self.nums[self.maxStack.top()] <= price:
            self.maxStack.pop()
        if self.maxStack.isEmpty():
            p = -1
        else:
            p = self.maxStack.top()
        self.maxStack.push(self.index)
        self.nums.append(price)
        return self.index - p
