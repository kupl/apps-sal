class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.incre = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.incre.append(0)

    def pop(self) -> int:
        if self.stack:
            if len(self.incre) > 1:
                self.incre[-2] += self.incre[-1]
            return self.stack.pop() + self.incre.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if self.incre:
            self.incre[min(len(self.incre), k) - 1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
