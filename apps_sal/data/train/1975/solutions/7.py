class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        

    def push(self, x: int) -> None:
        if len(self.stack) + 1 > self.maxSize:
            return
        self.stack.append(x)        

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        el = self.stack.pop()
        return el

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            self.stack = list([x+val for x in self.stack])
        else:
            beforek = list([x+val for x in self.stack[:k]])
            self.stack = beforek + self.stack[k:]

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

