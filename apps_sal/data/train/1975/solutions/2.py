class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.len = maxSize
    def push(self, x: int) -> None:
        if len(self.stack)+1 <= self.len:
            self.stack.append(x)
        
    def pop(self) -> int:
        if not self.stack: return -1
        last = self.stack[-1]
        self.stack = self.stack[:-1]
        return last

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            self.stack = [x+val for x in self.stack]
        else:
            self.stack[:k] = [x+val for x in self.stack[:k]]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

