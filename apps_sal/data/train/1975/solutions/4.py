class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxsize = maxSize

    def push(self, x: int) -> None:
        if self.maxsize == 0:
            return
        self.stack.append(x)
        self.maxsize -= 1

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        self.maxsize += 1
        return val

    def increment(self, k: int, val: int) -> None:
        self.stack[:k] = [x + val for x in self.stack[:k]]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
