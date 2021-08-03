class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.curSize = 0

    def push(self, x: int) -> None:
        if self.curSize < self.maxSize:
            self.stack.append(x)
            self.curSize += 1

    def pop(self) -> int:
        if self.stack:
            self.curSize -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        cur = 0
        while cur < k and cur < self.curSize:
            self.stack[cur] += val
            cur += 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
