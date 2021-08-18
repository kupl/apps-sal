class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.currSize = 0

    def push(self, x: int) -> None:
        if self.currSize < self.maxSize:
            self.stack.append(x)
            self.currSize += 1

    def pop(self) -> int:
        if self.currSize == 0:
            return -1
        else:
            self.currSize -= 1
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i <= k - 1 and i <= self.currSize - 1:
            self.stack[i] += val
            i += 1
