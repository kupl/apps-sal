class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.stack = list()

    def push(self, x: int) -> None:
        if len(self.stack) < self.max:
            self.stack.append([x, 0])

    def pop(self) -> int:
        if self.stack:
            (value, increment) = self.stack.pop()
            if self.stack:
                self.stack[-1][1] += increment
            return value + increment
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k <= len(self.stack):
            self.stack[k-1][1] += val
        else:
            if self.stack:
                self.stack[-1][1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

