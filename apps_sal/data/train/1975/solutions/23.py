class CustomStack:
    maxSz = 0
    stack = []

    def __init__(self, maxSize: int):
        self.maxSz = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSz:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            val = self.stack.pop(len(self.stack) - 1)
            return val
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i >= len(self.stack):
                return
            else:
                self.stack[i] += val
