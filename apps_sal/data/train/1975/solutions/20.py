class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top + 1 < len(self.stack):
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top < 0:
            return -1
        n = self.stack[self.top]
        self.top -= 1
        return n

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i <= self.top:
                self.stack[i] += val
